from divisors import lcm, is_coprime
from heapq import heappush, heappop

def perimeter_most_triples(limit):
	triples = []
	val = 1

	while True:
		maxn = 1
		while maxn > len(triples):
			perim = 4*maxn*maxn+6*maxn+2
			heappush(triples,(perim,maxn,maxn+1))

		p,n,m = heappop(triples)
		cur = lcm(val,p)
		if cur >= limit:
			return val
		val = cur

		m += 1
		while not is_coprime(n,m):
			m += 1
		if maxn < m-1:
			maxn = m-1

		p = 2*m*(m+n)
		heappush(triples,(p,n,m))


limit = 1000

result = perimeter_most_triples(limit)
print(result)

#print(lcm(665,1400))
#print(is_coprime(2,6))