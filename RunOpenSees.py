# Input
# OpenSees executable file path
PathOpenSees = "/home/chenting/Chenting/OpenSees3/bin/Pinching4Test/OpenSees"

# tcl file path
Pathtcl = "/home/chenting/Chenting/OpenSees3/bin/Pinching4Test/RCyclicPinch.tcl"

# Path to result file of displacement
PathDisp = "/home/chenting/Chenting/OpenSees3/bin/Pinching4Test/Disp.out"

# Which column is the displacement data? start from 0
ColumnDisp = 0

# Path to result file of force
PathForce = "/home/chenting/Chenting/OpenSees3/bin/Pinching4Test/Force.out"

# Which column is the force data? start from 0
ColumnForce = 0

# =====================================================================================================
# Program begins here

# Run OpenSees
import os
import time
os.system(PathOpenSees + " " + Pathtcl)

# Collect results
import matplotlib.pyplot as plt
time.sleep(2)

def File2List(filepath, column):
	content = open(filepath, 'r')
	returnlist = []
	for line in content:
		splited = line.split()
		if len(splited) > 0:
			number = float(splited[column])
			returnlist.append(number)
	return returnlist
	
disp = File2List(PathDisp, ColumnDisp)
force = File2List(PathForce, ColumnForce)

plt.figure(figsize=(6,6))
ax1 = plt.subplot(1, 1, 1)
p1 = plt.plot(disp, force, color='black', linestyle='-')

plt.show()
