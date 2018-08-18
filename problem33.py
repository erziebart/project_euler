import divisors as div

base = 10

fractions = []
reduced = []

for num in range(1,base):
	for den in range(num+1,base):
		val = num/den
		for digit in range(1,base):
			num1 = 10*num+digit
			den1 = 10*digit+den
			if num1/den1 == val:
				fractions.append((num1,den1))
				reduced.append((num,den))

			num2 = 10*digit+num
			den2 = 10*den+digit
			if num2/den2 == val:
				fractions.append((num2,den2))
				reduced.append((num,den))

print(fractions)
print(reduced)

num = 1
den = 1
for n,d in reduced:
	num *= n
	den *= d

num, den = div.reduce_frac(num,den)
print(num,"/",den)