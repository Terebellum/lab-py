import math

a = 10.2
b = 9.2
x = float(input())
c = 0.5
f = math.log(a+x**2)+ math.sin(x/6)**2
z = math.exp(-c*x)*math.sqrt(x+math.sqrt(x+a))/(x-math.sqrt(x-b))
print("f= ", f)
print("z= ", z)