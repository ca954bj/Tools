TheLast = 50

class Reorder:
	def __init__(self, olist):
		self.olist = olist
		self.length = len(self.olist)
		for i in range(1, self.length+1):
			if not i == self.olist[i - 1]:
				print("The old list is not correct, please check it!")
		self.nlist = range(1, self.length + 1, 1)
			
			
	def AddAfter(self, AfterWhichNumber):
		self.nlist.insert(AfterWhichNumber, AfterWhichNumber + 1)
		self.olist.insert(AfterWhichNumber, "None")
		self.length += 1
		for i in range((AfterWhichNumber + 1), self.length, 1):
			self.nlist[i] += 1
	
	def Delete(self, WhichToDelete):
		del self.nlist[WhichToDelete - 1]
		for i in range(WhichToDelete, self.length, 1):
			self.nlist[i] -= 1
	
	def ChangePosition(self, OldNumber, AfterWhichNumber):
		j = 0
		for i in range(AfterWhichNumber, OldNumber):
			self.nlist[AfterWhichNumber] = OldNumber + j
			j += 1
		
	def Print(self):
		for i in range(0, self.length):
			print(self.olist[i], self.nlist[i])

olist = range(1, TheLast + 1, 1)
RO1 = Reorder(olist)
RO1.AddAfter(10)
RO1.ChangePosition(20, 12)
RO1.Print()


