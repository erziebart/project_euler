import combinatorics as c

n = 10
digits = [x for x in range(n)]
idx = 999999

size = c.factorial(n)
result = ""
for i in range(n, 0, -1):
	size //= i
	region = idx//size
	result += str(digits.pop(region))
	idx -= region*size

print(result)
