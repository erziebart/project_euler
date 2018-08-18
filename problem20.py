import combinatorics as c

num = str(c.factorial(100))
s = 0
for digit in num:
	s += int(digit)
print(s)