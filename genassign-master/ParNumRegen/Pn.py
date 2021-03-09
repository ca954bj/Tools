import xlrd
import numpy as np

fnameC = "studentsClayton.xlsx"
fnameM = "studentsMalaysia.xlsx"
fnameNew = "CIV3221 & CIV5121 Sem 2 2020 results.xls"

tabC = "studentsClayton"
tabM = "studentsMalaysia"
tabNew = "CIV3221"

# Read Clayton Full namelist
wb1 = xlrd.open_workbook(fnameC)
sheet1 = wb1.sheet_by_name(tabC)
pnset = []
idset = []
for i in range(1, 311):
    pn = sheet1.cell_value(i, 0)
    pn = int(pn.split()[1])
    id1 = sheet1.cell_value(i, 3)
    id1 = int(id1)
    pnset.append(pn)
    idset.append(id1)
    
# Read Sunway Full namelist
wb2 = xlrd.open_workbook(fnameM)
sheet2 = wb2.sheet_by_name(tabM)
for i in range(1, 66):
    pn = sheet2.cell_value(i, 0)
    pn = int(pn.split()[1])
    id1 = sheet2.cell_value(i, 3)
    id1 = int(id1)
    pnset.append(pn)
    idset.append(id1)

# Read New namelist
wbnew = xlrd.open_workbook(fnameNew)
sheetnew = wbnew.sheet_by_name(tabNew)
TID = []
TPN = []
for i in range(1, 37):
    id1 = sheetnew.cell_value(i, 1)
    id1 = int(id1)
    TID.append(id1)

wbnew = xlrd.open_workbook(fnameNew)
sheetnew = wbnew.sheet_by_name(tabNew)
TID = []
TPN = []
for i in range(1, 37):
    id1 = sheetnew.cell_value(i, 1)
    id1 = int(id1)
    TID.append(id1)

for i, obj in enumerate(TID):
    for j, obj2 in enumerate(idset):
        if obj2 == obj:
            TPN.append(pnset[j])
            break
print(TPN)

# write data
fn = "PN.txt"
fl = open(fn, 'w')
for obj in TPN:
    fl.write("Participant " + str(obj))
    fl.write("\n")
fl.close()
