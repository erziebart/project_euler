import math

n = 1000

# multiples of 3 less than n
x = math.floor((n-1)/3)
c_3 = 3*x*(x+1)/2

# multiples of 5 less than n
x = math.floor((n-1)/5)
c_5 = 5*x*(x+1)/2

# multiples of 15 less than n
x = math.floor((n-1)/15)
c_15 = 15*x*(x+1)/2

print(c_3+c_5-c_15)