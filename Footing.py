# This file is for footing design
# Unit: m, N, Pa, kg, s

import xlrd
import time

class Footing:
	def __init__(self, Xc, Yc, DL, LL):
		# Xc is the length of the base plate (in the direction related to bending)
		# Yc is the width of the base plate(in the direction unrelated to bending)
		# DL is the dead load
		# LL is the live load
		# psoil is the allowable soil pressure
		
		self.Xc = Xc
		self.Yc = Yc
		self.DL = DL
		self.LL = LL

		
	def CheckBending(self, D, d, Xf, Yf, Ast, fsy, fc):
		# D is the depth of the footing
		# d is the depth to the center of steel bars
		# Xf is the length of the footing (in the direction related to the bending)
		# Yf is the width of the footing (in the direction unrelated to the bending)
		# Ast is the area of steel bars
		# fsy is the yield capacity of the steel bar
		# fc is the compressive strength of the concrete
		fsy = fsy * 1e6
		fc = fc * 1e6

		print("Soil Pressure:")
		self.psoil = (1.2 * self.DL + 1.5 * self.LL)/(Xf*Yf)
		print("Soil Pressure p = %f" % self.psoil)
		
		print("Checking Bending Capacity...\n")

		# Effective Width
		b = Yf
		print("Effective Width: %.3f" % b)
		
		# Checking reinforcement ratio
		p = float(Ast)/(d*b)
		print("Designed Reinforcement Ratio:")
		print("p = Ast / (d * b) = %.3f / (%.3f * %.3f) = %f\n" % (Ast, d, b, p))
		
		fcf = 0.6*((fc/1e6)**0.5)
		pmin = 0.2*((float(D)/d)**2)*fcf/(fsy/1e6)
		print("Minimum Reinforcement Ratio:")
		print("fcf = 0.6*fc**0.5 = 0.6*%.3f**0.5 = %.3f" % (fc/1e6, fcf))
		print("pmin = 0.2*(D/d)**2*fcf/fsy = 0.2*(%.3f/%.3f)**2*%.3f/%.3f = %f\n" % (D, d, fcf, fsy/1e6, pmin))
		
		if p < pmin:
			print("Error: Your design reinforcement Ratio is less than mimimum requirement!\n")
		else:
			print("Reinforcement Ratio is OK\n")
			
		# Checking Bending Capacity
		Mu = 0.8 * Ast * fsy * d * (1 - p * fsy / (1.7 * fc))/1000
		print("Bending Capacity:")
		print("Mu = 0.8 * Ast * fsy * d * (1 - p * fsy / (1.7 * fc)) = 0.8 * %.3f * %.3f * %.3f * (1 - %.3f * %.3f / (1.7 * %.3f)) = %.3f kN*m\n" % (Ast, fsy, d, p, fsy, fc, Mu))
		
		# Design Moment
		M = self.psoil * Yf * (float(Xf - self.Xc)/2)**2 / 2000
		print("Design Moment:")
		print("M = psoil * Yf * ((Xf - Xc)/2)**2 / 2 = %.3f * %.3f * ((%.3f - %.3f)/2)**2 / 2 = %f kN*m\n" % (self.psoil, Yf, Xf, self.Xc, M))
		
		# Compare between design moment and bending capacity
		if Mu < M:
			print("Error: Your design moment is less than bending capacity\n")
		else:
			print("Bending Check: Pass\n")

		print("======================================\n")
		# Checking Shear Failure
		print("Checking for Shear Failure ...\n")
		
		beta1 = 1.1 * (1.6 - d)
		print("beta1 = 1.1 * (1.6 - d) = 1.1 * (1.6 - %.3f) = %f\n" % (d, beta1))
		
		if beta1 < 1.1:
			beta1 = 1.1
			print("Because beta1 < 1.1, take beta1 = 1.1\n")
			
		# Shear Capacity
		Vuc = 0.7 * beta1 * b * d * 1e3 * (Ast * fc / (b * d * 1e6))**(1.0/3)
		print("Shear Capacity:")
		print("Vuc = 0.7 * beta1 * b * d * (Ast * fc / (b * d))**(1.0/3) = 0.7 * %.3f * %.3f * %.3f * (%.3f * %.3f / (%.3f * %.3f))**(1.0/3) = %f kN\n" % (beta1, b*1e3, d*1e3, Ast*1e6, fc/1e6, b*1e3, d*1e3, Vuc))
		
		# Design Shear
		V = self.psoil * Yf * ((Xf - self.Xc) / 2 - d) / 1000
		print("Design Shear:")
		print("V = q * Yf * ((Xf - Xc) / 2 - d) = %.3f * %.3f * ((%.3f - %.3f) / 2 - %.3f) = %f kN\n" % (self.psoil, Yf, Xf, self.Xc, d, V))
		
		# Compare between design shear and shear capacity
		if V < 0.5*Vuc and D < 0.75:
			print("Shear strength is OK, No ligs required\n")
		else:
			print("Warning: Insufficient shear strength, ligs are required!\n")
			
		# Checking Punching Shear Failure

		print("======================================\n")
		
		print("Checking for Shear Failure ...\n")
		
		# Punching Shear Capacity
		print("Punching Shear Capacity:")
		u = 2*(self.Xc + d) + 2*(self.Yc + d)
		Vuo = 0.7 * u * d * 0.34 * (fc/1e6)**0.5*1000
		print("u = 2*(Xc + d) + 2*(Yc + d) = 2*(%.3f + %.3f) + 2*(%.3f + %.3f) = %f" % (self.Xc, d, self.Yc, d, u))
		print("Vuo = 0.7 * u * d * 0.34 * fc**0.5 = 0.7 * %.3f * %.3f * 0.34 * %.3f**0.5 = %f kN\n" % (u, d, fc/1e6, Vuo))
		
		print("Design Punching Shear:")	
		V = (self.psoil*(Xf*Yf) - self.psoil*(self.Xc + d)*(self.Yc + d))/1000
		print("V = q*(Xf*Yf) - q*(Xc + d)*(Yc + d) = %.3f*(%.3f*%.3f) - %.3f*(%.3f + %.3f)*(%.3f + %.3f) = %f kN\n" % (self.psoil, Xf, Yf, self.psoil, self.Xc, d, self.Yc, d, V))
		
		# Compare
		if V < Vuo:
			print("Punching Shear Strength is OK\n")
			
		else:
			print("Error: Insufficient Punching Shear Strength\n")
			
book = xlrd.open_workbook("FootingDesign.xlsx")
first_sheet = book.sheet_by_index(0)
cell = first_sheet.cell(0,1)
Xc = float(cell.value)

cell = first_sheet.cell(1,1)
Yc = float(cell.value)

cell = first_sheet.cell(2,1)
if type(cell.value) != float and type(cell.value) != int:
	cellx = first_sheet.cell(2,3)
	DL = 0
	LL = float(cellx.value)/1.5
else:
	DL = float(cell.value)

	cell = first_sheet.cell(3,1)
	LL = float(cell.value)

cell = first_sheet.cell(5,1)
D = float(cell.value)

cell = first_sheet.cell(6,1)
d = float(cell.value)

cell = first_sheet.cell(7,1)
Xf = float(cell.value)

cell = first_sheet.cell(8,1)
Yf = float(cell.value)

cell = first_sheet.cell(9,1)
Ast = float(cell.value)

cell = first_sheet.cell(10,1)
fsy = float(cell.value)

cell = first_sheet.cell(11,1)
fc = float(cell.value)

#def __init__(self, Xc, Yc, DL, LL, psoil):
# Xc is the length of the base plate (in the direction related to bending)
# Yc is the width of the base plate(in the direction unrelated to bending)
# DL is the dead load
# LL is the live load
Footing1 = Footing(Xc, Yc, DL, LL)


#def CheckBending(self, D, d, Xf, Yf, Ast, fsy, fc):
# D is the depth of the footing
# d is the depth to the center of steel bars
# Xf is the length of the footing (in the direction related to the bending)
# Yf is the width of the footing (in the direction unrelated to the bending)
# Ast is the area of steel bars
# fsy is the yield capacity of the steel bar (MPa)
# fc is the compressive strength of the concrete (MPa)
Footing1.CheckBending(D, d, Xf, Yf, Ast, fsy, fc)
time.sleep(420)
