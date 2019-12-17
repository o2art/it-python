x1 = float(input("Podaj x początkowy pierwszego odcinka: "))
y1 = float(input("Podaj y początkowy pierwszego odcinka: "))
x2 = float(input("Podaj x końcowy pierwszego odcinka: "))
y2 = float(input("Podaj y końcowy pierwszego odcinka: "))
x3 = float(input("Podaj x początkowy drugiego odcinka: "))
y3 = float(input("Podaj y początkowy drugiego odcinka: "))
x4 = float(input("Podaj x końcowy drugiego odcinka: "))
y4 = float(input("Podaj y końcowy drugiego odcinka: "))

if (x1 == x2 and y1 == y2) or (x3 == x4 and y3 == y4):
    print("Odcinek nie może mieć zerowej długości.")
else:
    if x1 != x2 and x3 != x4:
        a1 = (y1 - y2) / (x1 - x2)
        b1 = y1 - (a1 * x1)

        a2 = (y3 - y4) / (x3 - x4)
        b2 = y3 - (a2 * x3)

        if a1 != a2:
            x = (b2 - b1) / (a1 - a2)
            y = a1 * x + b1
            if (x < x1 and x < x2) or (x > x1 and x > x2) or (
                    x < x3 and x < x4) or (x > x3 and x > x4):
                print("Odcinki się nie przecinają.")
            else:
                print("Odcinki się przecinają.")
        else:
            print("Odcinki się nie przecinają.")
    elif x1 == x2 and x3 != x4:
        a = (y3 - y4) / (x3 - x4)
        b = y3 - (a * x3)

        y = x1 * a + b
        if (y < y1 and y < y2) or (y > y1 and y > y2):
            print("Odcinki się nie przecinają.")
        else:
            if (x1 < x3 and x1 < x4) or (x1 > x3 and x1 > x4):
                print("Odcinki się nie przecinają.")
            else:
                print("Odcinki się przecinają.")
    elif x1 != x2 and x3 == x4:
        a = (y1 - y2) / (x1 - x2)
        b = y1 - (a * x1)

        y = x3 * a + b
        if (y < y3 and y < y4) or (y > y3 and y > y4):
            print("Odcinki się nie przecinają.")
        else:
            if (x3 < x1 and x3 < x2) or (x3 > x1 and x3 > x2):
                print("Odcinki się nie przecinają.")
            else:
                print("Odcinki się przecinają.")
    else:
        print("Odcinki się nie przecinają.")  #Bo sie pokrywają ewentualnie