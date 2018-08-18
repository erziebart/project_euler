import math

digits = 1000

phi = 0.5*(1 + math.sqrt(5))
result = math.ceil((digits - 1 + math.log10(math.sqrt(5)))/(math.log10(phi)))
print(result)