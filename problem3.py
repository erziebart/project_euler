import miller_rabin as pt
import math

n = 600851475143
f = n

# find largest odd factor
while f % 2 == 0:
	f /= 2

# divide out smallest odd prime factor until f is 1
p = 3
while not f==1:
	while (not pt.is_prime(p) or f%p != 0):
		p += 2
	while f % p == 0:
		f /= p

print(p)