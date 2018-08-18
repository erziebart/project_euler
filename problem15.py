import combinatorics as c

# nxn grid
n = 20

result = 1
for i in range(n):
	result //= i+1
	result *= 4*i+2

print(result)