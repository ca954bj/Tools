def NumberList(Copied, EmptyList):
	numbers = Copied.split()
	for obj in numbers:
		EmptyList.append(float(obj))
