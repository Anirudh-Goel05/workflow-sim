
def genPrimes():
	ulim = 1000000
	num = []
	for i in range(2,len(ulim)):
		x=i
		for j in range(2,i):
			x/=j
		if x==1:
			num.append(x)

	return num	
