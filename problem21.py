import divisors as div
import heapq

def d(n):
	return sum(div.proper_divisors(n))

n = 10000

amicable = []

for a in range(2,n):
	if a in amicable:
		continue

	b = d(a)
	if b > a and a == d(b):
		amicable.append(a)
		amicable.append(b)

print(sum([x for x in amicable if x < n]))


#print(d.factorize(9999))
#print(d.prime_factors(9999))
#print(sum(div.proper_divisors(5564)))