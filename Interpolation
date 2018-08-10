def LinearInterpolation2D(x1, y1, x2, y2, xi, tol=0.01):
    if abs(x1 - xi) < tol:
        return y1
    elif abs(x2 - xi) < tol:
        return y2
    else:
        k = (y2 - y1)/(x2 - x1)
        yi = k*(xi - x1) + y1
        return yi

def LinearInterpolation3D(x1, y1, z1, x2, y2, z2, x3, y3, z3, xi, yi, tol=0.01):
    if abs(x1 - xi) < tol and abs(y1 - yi) < tol:
        return z1
    elif abs(x2 - xi) < tol and abs(y2 - yi) < tol:
        return z2
    elif abs(x3 - xi) < tol and abs(y3 - yi) < tol:
        return z3
    else:
        return (x1*y2*z3 - x1*y3*z2 + x1*yi*z2 - x1*yi*z3 - x2*y1*z3 + x2*y3*z1 - x2*yi*z1 + x2*yi*z3 + x3*y1*z2 - x3*y2*z1 + x3*yi*z1 - x3*yi*z2 - xi*y1*z2 + xi*y1*z3 + xi*y2*z1 - xi*y2*z3 - xi*y3*z1 + xi*y3*z2)/(x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2)

'''from sympy import *
x1, y1, z1, x2, y2, z2, x3, y3, z3, xi, yi, zi = symbols('x1, y1, z1, x2, y2, z2, x3, y3, z3, xi, yi, zi')
v1 = [x2 - x1, y2 - y1, z2 - z1]
v2 = [x3 - x1, y3 - y1, z3 - z1]
v3 = [x3 - xi, y3 - yi, z3 - zi]
M = Matrix([v1, v2, v3])
DM = det(M)
print(DM)
zz = solve(DM, zi)
print(zz)'''

### ==================== Have a try ================================

'''yi = LinearInterpolation3D(0, 0, 0, 1, 0, 1, 0, 1, 2, 0.5, 0.5)
print(yi)'''
