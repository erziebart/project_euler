import divisors as div

def is_abundant(n):
	return sum(div.proper_divisors(n)) > n

limit = 28123
s = 0
abundant = []
for n in range(1,limit):
	i = 0
	j = len(abundant)-1
	while i <= j:
		res = abundant[i]+abundant[j]
		if res == n:
			break
		elif res < n:
			i += 1
		else:
			j -= 1
	if i > j:
		s += n

	if is_abundant(n):
		abundant.append(n)

#print(abundant)
print(s)