import math

def is_palindrome_b10(num):
	i = 0
	j = len(num)-1
	while i < j:
		if not num[i] == num[j]:
			return False
		i += 1
		j -= 1
	return True

def is_palindrome_b2(n):
	i = 0x80000000
	j = 0x1

	while n&i == 0 and i > j:
		i >>= 1

	while i > j:
		if (not n&i) != (not n&j):
			return False
		i >>= 1
		j <<= 1

	return True

limit = 1000000
ls = []
for n in range(1,limit,2):
	if is_palindrome_b10(str(n)) and is_palindrome_b2(n):
		ls.append(n)

print(ls)
print(sum(ls))