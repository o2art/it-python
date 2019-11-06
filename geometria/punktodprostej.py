import math

print("P(x,y), l: Ax+By+C=0\n")

x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))

A = int(input("Podaj współczynnik A: "))
B = int(input("Podaj współczynnik B: "))
C = int(input("Podaj współczynnik C: "))

if A != 0 and B != 0:
    d = abs(A*x+B*y+C) / math.sqrt(pow(A, 2) + pow(B, 2))
else:
    print("Prosta l ma równanie x=", C, sep="")

if d == 0:
    print("P(", x, ",", y, ") lezy na prostej l: ", A, "x+", B, "y+", C, sep="")
else:
    print("P(", x, ",", y, ") nie lezy na prostej l: ",
          A, "x+", B, "y+", C, sep="")
