iterator = 100
import math
def main():
	def allocation(aa, b):
		length = len(aa)
		product = []
		result = []
		fullproduct = 1
		for obj in aa:
			fullproduct = fullproduct * obj
		for i in range(1, length):
			product.append(1)
			for i in range(i, length):
				product[-1] = product[-1] * aa[i]
		r1= b%fullproduct
		for i in range(1, length):
			d1 = int(r1/product[i - 1])
			r1 = r1%product[i - 1]
			result.append(d1)
		result.append(r1)
		return result
	
	# ============================= Question 2 ============================
	para2_1 = [4, 3]
	para2_2 = [3, 3, 3]
	al2_1 = allocation(para2_1, iterator)
	al2_2 = allocation(para2_2, iterator)
		
	select21 = al2_1[0]
	select22 = al2_1[1]
	select23 = al2_2[0]
	select24 = al2_2[1]
	select25 = al2_2[2]
	v21 = [2.8, 3, 3.2, 3.4]
	v22 = [3.5, 4.5, 5]
	v23 = [1.5, 2.5, 3.5]
	v24 = [20, 30, 40]
	v25 = [0.5, 0.8, 1.1]
	
	sv21 = v21[select21]
	sv22 = v22[select22]
	sv23 = v23[select23]
	sv24 = v24[select24]
	sv25 = v25[select25]
	
	# ============================= Question 3 ============================
	para3_1 = [4, 4]
	para3_2 = [4]
	al3_1 = allocation(para3_1, iterator)
	v31 = [3, 3.5, 4, 4.5]
	v32 = [0.5, 1, 1.5, 2]
	v33 = [7800, 8000, 8200, 8400]
	
	sv31 = v31[al3_1[0]]
	sv32 = v32[al3_1[1]]
	sv33 = v33[iterator%4]
	
	# ============================= Question 4 ============================
	para4_1 = [3, 3]
	para4_2 = [4, 4]
	al4_1 = allocation(para4_1, iterator)
	al4_2 = allocation(para4_2, iterator)
	v41 = [400, 450, 500]
	v42 = [350, 400, 450]
	v43 = [1500, 1700, 1900, 2100]
	v44 = [1500, 1700, 1900, 2100]
	
	sv41 = v41[al4_1[0]]
	sv42 = v42[al4_1[1]]
	sv43 = v43[al4_2[0]]
	sv44 = v44[al4_2[1]]
	
	# ============================= Question 5 ============================
	para5_1 = [5, 4, 4]
	al5_1 = allocation(para5_1, iterator)
	para5_2 = [2, 2, 2, 2]
	al5_2 = allocation(para5_2, iterator)
	v51 = [3, 3.2, 3.4, 3.6, 4]
	v52 = [6, 6.2, 6.4, 6.6]
	v53 = [280, 300, 320, 350]
	v54 = [60, 80]
	v55 = [0.8, 0.9]
	v56 = [150, 200]
	v57 = [0.8, 0.9]
	
	sv51 = v51[al5_1[0]]
	sv52 = v52[al5_1[1]]
	sv53 = v53[al5_1[2]]
	sv54 = v54[al5_2[0]]
	sv55 = v55[al5_2[1]]
	sv56 = v56[al5_2[2]]
	sv57 = v57[al5_2[3]]
	
main()
