import math

xA = float(input("Podaj współrzędną x1: "))
yA = float(input("Podaj współrzędną y1: "))
xB = float(input("Podaj współrzędną x2: "))
yB = float(input("Podaj współrzędną y2: "))
xP = float(input("Podaj współrzędną x3: "))
yP = float(input("Podaj współrzędną y3: "))

if xA <= xP <= xB:
    if yA <= yP <= yB:
        print('Punkty (' + str(xP) + ', ' + str(yP) + ') należą do obszaru')
    else:
        print('Punkty (' + str(xP) + ', ' + str(yP) + ') nie należą do obszaru')
elif xB <= xP <= xA:
    if yB <= yP <= yA:
        print('Punkty (' + str(xP) + ', ' + str(yP) + ') należą do obszaru')
    else:
        print('Punkty (' + str(xP) + ', ' + str(yP) + ') nie należą do obszaru')
else:
    print('Punkty (' + str(xP) + ', ' + str(yP) + ') nie należą do obszaru')
