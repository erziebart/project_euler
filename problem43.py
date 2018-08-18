from problem38 import reverse_pandigitals

divisors = [2,3,5,7,11,13,17]

s = 0
digits = [x for x in range(0,10)]
for n in reverse_pandigitals(digits):
	success = True
	for i in range(1,len(n)-2):
		success &= int(n[i:i+3])%divisors[i-1] == 0
	if success:
		print(n)
		s += int(n)

print(s)