import combinatorics as c

factorial = [c.factorial(n) for n in range(0,10)]

limit = 7*factorial[9]

nums = []
for n in range(3,limit):
	s = sum([factorial[int(d)] for d in str(n)])
	if s == n: nums.append(n)

print(nums)
print(sum(nums))