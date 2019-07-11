# A set of data must be in a horizontal line
# The first line is a reference line
# Other lines are data sets to be handled
fn = ""

# =================================================== Begin =============================================
content = open(fn, 'r')
Ref = []
Data = {}
Ref2 = []
Data2 = {}
linen = 0
for line in content:
	linen = linen + 1
	sp = line.split()
	length = len(sp)
	if length > 0 and linen == 1:
		for obj in sp:
			Ref.append(float(obj))
	elif length > 0:
		Data[linen] = []
		Data2[linen] = [0]
		for obj in sp:
			Data[linen].append(float(obj))

linenlast = linen

CurrentRef = Ref[0]
Ref2 = Ref[0]
counter = 0
for i, obj in enumerate(Ref):
	if obj == CurrentRef:
		counter = counter + 1
		for j in range(2, linenlast + 1):
			Data2[j][-1] = Data2[j][-1] + Data[j][i]
	else:
		Ref2.append(obj)
		for j in range(2, linenlast + 1):
			Data2[j][-1] = Data2[j][-1]/counter
			Data2[j].append(0)
			Data2[j][-1] = Data2[j][-1] + Data[j][i]
		counter = 1
		
print(Data2)
	

