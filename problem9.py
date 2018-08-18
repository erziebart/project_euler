import math

s = 1000

if s % 2 != 0:
	print('no solutions')
else:
	s /= 2

done = False
limit_n = math.ceil(0.25*(math.sqrt(1+8*s)-3))
for n in range(1, limit_n):

	limit_m = math.ceil(0.5*(math.sqrt(n*n+4*s)-n))
	for m in range(n+1, limit_m, 2):
		p = m + n
		r = s % (m * p)
		if r == 0:
			k = s // (m * p)
			done = True
			break

	if done:
		break

if done:
	print(m,n)
	a = k*(m*m-n*n)
	b = k*2*m*n
	c = k*(m*m+n*n)
	print(a,b,c)
	print(a*b*c)
else:
	print('no solutions')