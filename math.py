import math
x = 1.7
a = 0.5
b = 1.08
c = 2.1
m = 0.7
s = (math.sin(x)/math.sqrt(1+math.pow(m,2)-math.pow(math.sin(x),2)) - c*m)
print(s)