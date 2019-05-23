tol = 0.01

class Point:
  instances = []
  counter = 1
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    flag = 0
    for i in range(0, Point.counter-1):
      if abs(Point.instances[i].x - self.x) < tol and abs(Point.instances[i].y - self.y) < tol and abs(Point.instances[i].z - self.z) < tol:
        flag = 1
    if flag == 0:
      self.n = Point.counter
      Point.instances.append(self)
      Point.counter += 1

class Line:
  def __init__(self, A, B):
    self.A = A
    self.B = B

    if abs(A.x - B.x) < tol and abs(A.y - B.y) < tol and abs(A.z - B.z) >= tol:
      contain = filter(lambda xx: abs(xx.x - A.x) < tol and abs(xx.y - A.y) < tol and (xx.z - A.z)*(xx.z - B.z) <= 0, Point.instances)
      contain = sorted(contain, key = lambda xx: xx.z)
    elif abs(A.x - B.x) < tol and abs(A.z - B.z) < tol and abs(A.y - B.y) >= tol:
      contain = filter(lambda xx: abs(xx.x - A.x) < tol and abs(xx.z - A.z) < tol and (xx.y - A.y)*(xx.y - B.y) <= 0, Point.instances)
      contain = sorted(contain, key = lambda xx: xx.y)
    elif abs(A.y - B.y) < tol and abs(A.z - B.z) < tol and abs(A.x - B.x) >= tol:
      contain = filter(lambda xx: abs(xx.y - A.y) < tol and abs(xx.z - A.z) < tol and (xx.x - A.x)*(xx.x - B.x) <= 0, Point.instances)
      contain = sorted(contain, key = lambda xx: xx.x)
    
    self.contain = contain

  def contain(self):
    return self.contain
    
class WritePoints:
  def __init__(self, File):
    for obj in Point.instances:
      File.write("K, %d, %f, %f, %f\n"%(obj.n, obj.x, obj.y, obj.z))

class Link:
  def __init__(self, PointList, File):
    length = len(PointList)
    for i in range(1, length):
      File.write("L, %d, %d\n" % (PointList[i-1].n, PointList[i].n))
      
class FindPoint:
  def __init__(self, x, y, z):
    self.found = filter(lambda xx: abs(xx.x - x)<tol and abs(xx.y - y)<tol and abs(xx.z - z)<tol, Point.instances)[0]
  def found(self):
    return self.found

File=open("Points&Lines.txt",'w')

for i in range(0, 21):
  Point(0.45*i, 0, 0)
  Point(0.45*i, 2.9, 0)
  
for i in range(0, 11):
  Point(0.9*i, 0, 2.4)
  Point(0.9*i, 2.9, 2.4)
  
for i in range(0, 6):
  Point(0.6*i, 0, 0)
  Point(0.6*i, 0, 2.4)
  Point(3+0.6*i, 0, 0)
  Point(3+0.6*i, 0, 2.4)
  Point(6+0.6*i, 0, 0)
  Point(6+0.6*i, 0, 2.4)
  Point(6+0.6*i, 2.9, 0)
  Point(6+0.6*i, 2.9, 2.4)
  
for i in range(0, 4):
  Point(0, 0.5+0.6*i, 0)
  Point(0, 0.5+0.6*i, 2.4)
  Point(9, 0.5+0.6*i, 0)
  Point(9, 0.5+0.6*i, 2.4)
  
WritePoints(File)

P1 = FindPoint(0, 0, 0).found
P2 = FindPoint(9, 0, 0).found
Line1 = Line(P1, P2).contain
Link(Line1, File)

P1 = FindPoint(0, 0, 2.4).found
P2 = FindPoint(9, 0, 2.4).found
Line1 = Line(P1, P2).contain
Link(Line1, File)

P1 = FindPoint(0, 2.9, 0).found
P2 = FindPoint(9, 2.9, 0).found
Line1 = Line(P1, P2).contain
Link(Line1, File)

P1 = FindPoint(0, 2.9, 2.4).found
P2 = FindPoint(9, 2.9, 2.4).found
Line1 = Line(P1, P2).contain
Link(Line1, File)

for i in range(0, 16):
  P1 = FindPoint(i*0.6, 0, 0).found
  P2 = FindPoint(i*0.6, 0, 2.4).found
  Line1 = Line(P1, P2).contain
  Link(Line1, File)
  
P1 = FindPoint(0, 2.9, 0).found
P2 = FindPoint(0, 2.9, 2.4).found
Line1 = Line(P1, P2).contain
Link(Line1, File)

for i in range(0, 6):
  P1 = FindPoint(6 + i*0.6, 2.9, 0).found
  P2 = FindPoint(6 + i*0.6, 2.9, 2.4).found
  Line1 = Line(P1, P2).contain
  Link(Line1, File)
  
for i in range(0, 21):
  P1 = FindPoint(i*0.45, 0, 0).found
  P2 = FindPoint(i*0.45, 2.9, 0).found
  Line1 = Line(P1, P2).contain
  Link(Line1, File)
  
for i in range(0, 11):
  P1 = FindPoint(i*0.9, 0, 2.4).found
  P2 = FindPoint(i*0.9, 2.9, 2.4).found
  Line1 = Line(P1, P2).contain
  Link(Line1, File)
  
for i in range(0, 4):
  P1=FindPoint(0, 0.5+0.6*i, 0).found
  P2=FindPoint(0, 0.5+0.6*i, 2.4).found
  Line1 = Line(P1, P2).contain
  Link(Line1, File)
  
for i in range(0, 4):
  P1=FindPoint(9, 0.5+0.6*i, 0).found
  P2=FindPoint(9, 0.5+0.6*i, 2.4).found
  Line1 = Line(P1, P2).contain
  Link(Line1, File)
#CT = Line(A, D).contain
#for obj in CT:
  #print("%f, %f, %f\n"%(obj.x, obj.y, obj.z))
