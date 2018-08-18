# nxn grid
n = 1001

s = 1
c = 1
for i in range(1,(n+1)//2):
	intval = 2*i
	for j in range(4):
		c += intval
		s += c

print(s)