
# ==================================== Input ===================================
infile = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts8SF2StrainG7.txt"
outfile = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts8SF2StrainG7Avg.txt"
Tol = 1e-6

# ==============================================================================
X = []
Y = []
tempx = ""
sum = 0
account = 0
content = open(infile)
for line in content:
	sp = line.split()
	tempxn = float(sp[0])
	if type(tempx) == float and abs(tempx - tempxn) < Tol or tempx == "":
		sum += float(sp[1])
		account += 1
	else:
		X.append(tempx)
		Y.append(sum/account)
		sum = float(sp[1])
		account = 1
		
	tempx = tempxn
	
X.append(tempx)
Y.append(sum/account)
	
fn = open(outfile, 'w')
length = len(X)
for i in range(0, length):
	fn.write("%f %f\n" % (X[i], Y[i]))
	
fn.close()
