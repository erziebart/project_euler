import divisors as d

n = 500

i = 1
t = 1
while d.factor_count(t) < n:
	i += 1
	t += i

print(t)
print(d.factor_count(t))
print(d.prime_factors(t))