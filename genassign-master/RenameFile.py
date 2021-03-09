import os
filePath = "./"
for obj1, obj2, obj3 in os.walk(filePath):
	newobj = obj1 + '_'
	obj1_new = obj1.split('./')[1]
	newobj_new = newobj.split('./')[1]
	print(obj1_new)
	print(newobj_new)
	if len(obj1_new) > 5:
		os.rename(obj1_new, newobj_new)
	
