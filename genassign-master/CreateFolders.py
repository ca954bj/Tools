import pandas as pd
import os

currentpath = os.getcwd()
docxfile = currentpath + "/Trial file2.pdf"
newpath = currentpath + "/TestSubmit"
csv_filepath = "Grades-CIV5121_S2_2020-Practice for file scanning and uploading--7898722.csv"
try:
	os.mkdir(newpath)
except:
	print("folder not created")
df = pd.read_csv(csv_filepath)
total_students = df.shape[0]

print(df)

for i in range(0, total_students):
	sname, snumber = df['Identifier'][i].split()
	sname = df['Full name'][i]
	ID = df['ID number'][i]
	foldername = "{}_{}_assignsubmission_onlinetext_".format(sname, snumber)
	try:
		os.mkdir(newpath + '/' + foldername)
	except:
		print("subfolder not created")
		
	os.system('''cp "{}" "{}"'''.format(docxfile, newpath + '/' + foldername))

