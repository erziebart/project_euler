fib1 = 1
fib2 = 2
total = 0

while(fib2 <= 4E6):
	total += fib2
	fib0 = fib1+fib2
	fib1 = fib2+fib0
	fib2 = fib0+fib1

print(total)