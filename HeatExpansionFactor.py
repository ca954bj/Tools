import math

class ExpansionFactor:
  def __init__(self, Radius, Length, TemperatureChange, Preload, E):
    # Radius is the radius of the bolt
    # Length is the length of the bolt shank
    # TemperatureChange is the change of temperature in the predefined field
    # E is the Young's modulus of the bolt

    A = math.pi*Radius*Radius
    dl = Preload*Length/(E*A)
    self.alpha = dl/(Length*TemperatureChange)
  def alpha(self):
    return self.alpha



# Usage
#alpha = ExpansionFactor(18, 80, 1, 1000, 205000).alpha
alpha = ExpansionFactor(10, 16, 1, 156000, 205000).alpha
print(alpha)

