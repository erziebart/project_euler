import divisors as d

n = 10001

primes = [2]
m = 3

idx = 1
while idx < n:
	if not d.divides(primes, m):
		primes.append(m)
		idx += 1
	m += 2

print(n,"th prime is",primes[-1])