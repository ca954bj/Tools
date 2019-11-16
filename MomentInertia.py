class IBeam:
	def __init__(self, depth, width, tw, tf):
		width = float(width)
		depth = float(depth)
		self.MomentInertia = depth**3*width/12 + 2*tw*(depth/2 - tf)**3/3 - 2*width*(depth/2 - tf)**3/3
	def MomentInertia(self):
		return self.MomentInertia
	def Command(self, SectionID, MaterialID):
		line1 = 'section Fiber %d {\n' % SectionID
		line2 = '# PatchRect "LowerFlange": matTag NSIJ NSJK yI zI yJ zJ\n'
		line3 = 'patch rect %d 10 10 %f %f %f %f\n' % (MaterialID, -depth/2, -width/2, -depth/2 + tf, width/2)
		line4 = '# PatchRect "Web": matTag NSIJ NSJK yI zI yJ zJ\n'
		line5 = 'patch rect %d 10 10 %f %f %f %f\n' % (MaterialID, -depth/2 + tf, -tw/2, depth/2 - tf, tw/2)
		line6 = '# PatchRect "UpperFlange": matTag NSIJ NSJK yI zI yJ zJ\n'
		line7 = 'patch rect %d 10 10 %f %f %f %f\n' % (MaterialID, depth/2 - tf, -width/2, depth/2, width/2)
		line8 = '}\n'
		return line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8
	
class CompositeBeam:
	def __init__(self, depth, width, tw, tf, slabwidth, slabthick, Es, Ec):
		c1 = Ec*slabthick*slabwidth
		c2 = Es*tf
		self.offset = c1*(depth + slabthick)/(2*(c1 + Es*depth*tw - 2*c2*tw + 2*c2*width))
		self.slabthick = slabthick
		self.slabwidth = slabwidth
	def Offset(self):
		return self.offset
	def Command(self, SectionID, SteelMaterialID, ConcreteMaterialID):
		line1 = 'section Fiber %d {\n' % SectionID
		line2 = '# PatchRect "LowerFlange": matTag NSIJ NSJK yI zI yJ zJ\n'
		line3 = 'patch rect %d 10 10 %f %f %f %f\n' % (SteelMaterialID, -depth/2 - self.offset, -width/2, -depth/2 + tf - self.offset, width/2)
		line4 = '# PatchRect "Web": matTag NSIJ NSJK yI zI yJ zJ\n'
		line5 = 'patch rect %d 10 10 %f %f %f %f\n' % (SteelMaterialID, -depth/2 + tf - self.offset, -tw/2, depth/2 - tf - self.offset, tw/2)
		line6 = '# PatchRect "UpperFlange": matTag NSIJ NSJK yI zI yJ zJ\n'
		line7 = 'patch rect %d 10 10 %f %f %f %f\n' % (SteelMaterialID, depth/2 - tf - self.offset, -width/2, depth/2 - self.offset, width/2)
		line8 = '# PatchRect "Concrete": matTag NSIJ NSJK yI zI yJ zJ\n'
		line9 = 'patch rect %d 10 10 %f %f %f %f\n' % (ConcreteMaterialID, depth/2 - self.offset, -self.slabwidth/2, depth/2 - self.offset + self.slabthick, self.slabwidth/2)
		line10 = '}\n'
		return line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10
