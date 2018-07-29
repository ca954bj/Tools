import math

class StrainRossette:
  def __init__(self, StrainX, StrainS, StrainY):
    # StrainS should be in 45 degree direction
    length1 = len(StrainX)
    length2 = len(StrainY)
    length3 = len(StrainS)
    if length1 != length2 or length2 != length3 or length1 != length3:
      print("Three Strain Components should have same length")
    else:
      Angle = []
      Px = []
      Py = []
      VMS = []
      for i in range(0, length1):
        ShearStrain = -StrainX[i] + 2*StrainS[i] - StrainY[i]
        Angle.append(math.atan(ShearStrain/(StrainX[i] - StrainY[i]))*0.5)
        p1 = (StrainX[i] + StrainY[i])/2
        p2 = (((StrainX[i] - StrainY[i])/2)**2 + (ShearStrain/2)**2)**0.5
        Px.append(p1 + p2)
        Py.append(p1 - p2)
        VMS.append(2.0**0.5/3*((2*p2)**2 + (p1 + p2)**2 + (p1 - p2)**2)**0.5)

    self.Px = Px
    self.Py = Py
    self.Angle = Angle
    self.VMS = VMS

  def Px(self):
    # ============ Principal Strain 1 ================
    return self.Px

  def Py(self):
    # ============ Principal Strain 2 ===============
    return self.Py

  def Angle(self):
    return self.Angle

  def VMS(self):
    # ============== Equivalent Von-mises Strain =====================
    return self.VMS


# ================ ImportFile =========================
File = open('/media/chenting/Work/ProgramCode/StrainRossette/SX1-1StrainGuages.txt')
Px = []
Py = []
Angle = []
n = 0

for line in File:
  content = line.split()
  if len(content) == 3:
    n = n + 1
    Px.append(float(content[2]))
    Py.append(float(content[1]))
    Angle.append(float(content[0]))

File.close()

Result = StrainRossette(Px, Py, Angle)

File = open('/media/chenting/Work/ProgramCode/StrainRossette/SX1-1StrainGuagesResult.txt', 'w')
for i in range(0, n):
  File.write('%f %f %f %f\n' % (Result.Px[i], Result.Py[i], Result.Angle[i], Result.VMS[i]))

File.close()

