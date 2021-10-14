import math
a = int(input("Width: "))
b = int(input("Height"))
perim = 2*(a+b)
diag = math.sqrt(a**2+b**2)
print("Perimeter is ", perim)
print("Diagonal is ", diag)
