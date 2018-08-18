import combinatorics as c

def reverse_pandigitals(digits):
	n = len(digits)
	maximum = c.factorial(n)
	for idx in range(maximum-1, -1, -1):
		ls = digits.copy()
		size = maximum
		result = ""
		for i in range(n, 0, -1):
			size //= i
			region = idx//size
			result += str(ls.pop(region))
			idx -= region*size
		yield result


digits = [d for d in range(1,10)]
for num in reverse_pandigitals(digits):
	n = int(num)
	if n%100002 == 0:
		print(n//100002,"=>",num)
		break
