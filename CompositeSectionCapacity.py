from sympy import *

def MomentCapacity(Geometry, Material, curvature):
	NumComponent = len(Geometry)
	if len(Material) != NumComponent:
		print('Erorr in function MomentCapacity !!')
		return 0
	Moment = 0
	for i, obj1 in enumerate(Geometry):
		x1 = obj1[0]
		y1 = obj1[1]
		x2 = obj1[2]
		y2 = obj1[3]
		theMaterial = Material[i]
		length = abs(x2 - x1)
		width = abs(y2 - y1)
		stress = 
		integrate(width*)

x = symbols('x')
M1 = 205000*x
M2 = Piecewise((0, x>=0), (35000*x, x<0 and x >=-50.0/35000), (-50, x<-50.0/35000))
c = MomentCapacity([[-220, -110, -208, 110], [208, -110, 220, 110], [-208, 98, 208, 110], [-208, -110, 208, -98], [-208, -98, 208, 98]], [M1, M1, M1, M1, M2])
print(c)
