ostring = "13(4) (2011) 58-66"
splited = ostring.split()
p1 = splited[0]
p2 = splited[1]
p3 = splited[2]

newstring = p2[1:-1] + ';' + p1 + ':' + p3

print(newstring)