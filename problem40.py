import math
import operator

def champernowne(n):
	num = 1
	pos = 1
	res = 0

	while pos <= n:
		l = math.floor(math.log10(num)+1)
		if pos + l > n:
			res = int(str(num)[n-pos])
		pos += l
		num += 1

	return res

digits = [1,10,100,1000,10000,100000,1000000]
factors = []
product = 1

num = 1
pos = 1
for d in digits:
	while pos <= d:
		l = math.floor(math.log10(num)+1)
		if pos + l > d:
			f = int(str(num)[d-pos])
			factors.append(f)
			product *= f
			break
		else:
			pos += l
			num += 1


print(factors)
print(product)