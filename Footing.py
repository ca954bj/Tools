# This file is for footing design
# Unit: m, N, Pa, kg, s

class Footing:
	def __init__(self, Xc, Yc, DL, LL, psoil):
		# Xc is the length of the base plate (in the direction related to bending)
		# Yc is the width of the base plate(in the direction unrelated to bending)
		# DL is the dead load
		# LL is the live load
		# psoil is the allowable soil pressure
		
		self.Xc = Xc
		self.Yc = Yc
		self.DL = DL
		self.LL = LL
		self.psoil = psoil
		
	def CheckBending(self, D, d, Xf, Yf, Ast, fsy, fc):
		# D is the depth of the footing
		# d is the depth to the center of steel bars
		# Xf is the length of the footing (in the direction related to the bending)
		# Yf is the width of the footing (in the direction unrelated to the bending)
		# Ast is the area of steel bars
		# fsy is the yield capacity of the steel bar
		# fc is the compressive strength of the concrete
		
		print("Checking Bending Capacity...\n")
		
		# Checking reinforcement ratio
		p = float(Ast)/(d*Yf)
		print("Designed Reinforcement Ratio:")
		print("p = Ast / (d * Yf) = %.3f / (%.3f * %.3f) = %f\n" % (Ast, d, Yf, p))
		
		fcf = 0.6*(fc**0.5)
		pmin = 0.2*((float(D)/d)**2)*fcf/fsy
		print("Minimum Reinforcement Ratio:")
		print("fcf = 0.6*fc**0.5 = 0.6*%.3f**0.5 = %.3f" % (fc, fcf))
		print("pmin = 0.2*(D/d)**2*fcf/fsy = 0.2*(%.3f/%.3f)**2*%.3f/%.3f = %f\n" % (D, d, fcf, fsy, pmin))
		
		if p < pmin:
			print("Error: Your design reinforcement Ratio is less than mimimum requirement!\n")
		else:
			print("Reinforcement Ratio is OK\n")
			
		# Checking Bending Capacity
		Mu = 0.8 * Ast * fsy * d * (1 - p * fsy / (1.7 * fc))
		print("Bending Capacity:")
		print("Mu = 0.8 * Ast * fsy * d * (1 - p * fsy / (1.7 * fc)) = 0.8 * %.3f * %.3f * %.3f * (1 - %.3f * %.3f / (1.7 * %.3f)) = %.3f\n" % (Ast, fsy, d, p, fsy, fc, Mu))
		
		# Design Moment
		M = self.psoil * Yf * (float(Xf - self.Xc)/2)**2 / 2
		print("Design Moment:")
		print("M = psoil * Yf * ((Xf - Xc)/2)**2 / 2 = %.3f * %.3f * ((%.3f - %.3f)/2)**2 / 2 = %f\n" % (self.psoil, Yf, Xf, self.Xc, M))
		
		# Compare between design moment and bending capacity
		if 0.8*Mu < M:
			print("Error: Your design moment is less than bending capacity\n")
		else:
			print("Bending Check: Pass\n")
			
		# Checking Shear Failure
		print("Checking for Shear Failure ...\n")
		
		beta1 = 1.1 * (1.6 - d)
		print("beta1 = 1.1 * (1.6 - d) = 1.1 * (1.6 - %.3f) = %f\n" % (d, beta1))
		
		if beta1 < 1.1:
			beta1 = 1.1
			print("Because beta1 < 1.1, take beta1 = 1.1\n")
			
		# Shear Capacity
		Vuc = beta1 * Yf * d * (Ast * fc / (Yf * d))**(1.0/3)
		print("Shear Capacity:")
		print("Vuc = beta1 * Yf * d * (Ast * fc / (Yf * d))**(1.0/3) = %.3f * %.3f * %.3f * (%.3f * %.3f / (%.3f * %.3f))**(1.0/3) = %f\n" % (beta1, Yf, d, Ast, fc, Yf, d, Vuc))
		
		# Design Shear
		V = self.psoil * Yf * ((Xf - self.Xc) / 2 - d)
		print("Design Shear:")
		print("V = q * Yf * ((Xf - Xc) / 2 - d) = %.3f * %.3f * ((%.3f - %.3f) / 2 - %.3f) = %f\n" % (self.psoil, Yf, Xf, self.Xc, d, V))
		
		# Compare between design shear and shear capacity
		if V < 0.5*0.7*Vuc and D < 0.75:
			print("Shear strength is OK, No ligs required\n")
		else:
			print("Warning: Insufficient shear strength, ligs are required!\n")
			
		# Checking Punching Shear Failure
		
		print("Checking for Shear Failure ...\n")
		
		# Punching Shear Capacity
		print("Punching Shear Capacity:")
		u = 2*(self.Xc + d) + 2*(self.Yc + d)
		Vuo = 0.7 * u * d * 0.34 * fc**0.5
		print("u = 2*(Xc + d) + 2*(Yc + d) = 2*(%.3f + %.3f) + 2*(%.3f + %.3f) = %f" % (self.Xc, d, self.Yc, d, u))
		print("Vuo = 0.7 * u * d * 0.34 * fc**0.5 = 0.7 * %.3f * %.3f * 0.34 * %.3f**0.5 = %f\n" % (u, d, fc, Vuo))
		
		print("Design Punching Shear:")	
		V = self.psoil*(Xf*Yf) - self.psoil*(self.Xc + d)*(self.Yc + d)
		print("V = q*(Xf*Yf) - q*(Xc + d)*(Yc + d) = %.3f*(%.3f*%.3f) - %.3f*(%.3f + %.3f)*(%.3f + %.3f) = %f\n" % (self.psoil, Xf, Yf, self.psoil, self.Xc, d, self.Yc, d, V))
		
		# Compare
		if V < 0.7*Vuo:
			print("Punching Shear Strength is OK\n")
			
		else:
			print("Error: Insufficient Punching Shear Strength\n")
		
		
Footing1 = Footing(0.45, 0.45, 1000e3, 800e3, 200e3)
Footing1.CheckBending(0.8, 0.725, 3, 3, 19.52e-4, 500e6, 32e6)