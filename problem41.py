from problem38 import reverse_pandigitals
from divisors import is_prime_n

digits = [d for d in range(1,8)]
for n in reverse_pandigitals(digits):
	if is_prime_n(int(n)):
		print(n)
		break