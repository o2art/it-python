import math


class Punkt:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def odleglosc(self, b) -> float:
        return math.sqrt((b.x - self.x)**2 + (b.y - self.y)**2)


class Prosta:
    def __init__(self, A: float, B: float, C: float):
        self.A = A
        self.B = B
        self.C = C

    def zawierapunkt(self, p: Punkt) -> bool:
        if self.A != 0:
            return p.x == ((-self.B * p.y - self.C) / self.A)
        elif self.B != 0:
            return p.y == ((-self.A * p.x - self.C) / self.B)
        else:
            #print("Równanie nie przedstawia prostej.")
            return False


class Odcinek:
    def __init__(self, a: Punkt, b: Punkt):
        self.a = a
        self.b = b

    def dlugosc(self) -> float:
        return self.a.odleglosc(self.b)

    def prosta(self) -> Prosta:
        A = (self.b.y - self.a.y) / (self.b.x - self.a.x)
        C = self.a.y - self.a.x * A
        return Prosta(A, -1, C)

    def zawierapunkt(self, p: Punkt) -> bool:
        return p.odleglosc(self.a) + p.odleglosc(self.b) <= self.dlugosc() and self.prosta().zawierapunkt(p)


# Interface

def podajliczbe(msg):
    while True:
        try:
            liczba = float(input(msg))
            return liczba
        except:
            print("Podaj prawidłową liczbę.")

while True:
    odp = input("Chcesz sprawdzić położenie punktu względem odcinka[cokolwiek co nie jest Q/q] czy wyjść[Q/q]? ")
    if odp.lower() == "q":
        print("Żegnam.")
        break

    Ax = podajliczbe("Podaj współrzędną x punktu początkowego odcinka: ")
    Ay = podajliczbe("Podaj współrzędną y punktu początkowego odcinka: ")
    Bx = podajliczbe("Podaj współrzędną x punktu końcowego odcinka: ")
    By = podajliczbe("Podaj współrzędną y punktu końcowego odcinka: ")
    if Ax == Bx and Ay == By:
        print("Odcinek nie może mieć zerowej długości.")
        continue
    odc = Odcinek(Punkt(Ax, Ay), Punkt(Bx, By))

    x = podajliczbe("Podaj współrzędną x punktu: ")
    y = podajliczbe("Podaj współrzędną y punktu: ")
    p = Punkt(x, y)

    if odc.zawierapunkt(p):
        print("Punkt ten leży na tym odcinku.")
    else:
        print("Punkt ten nie leży na tym odcinku.")
    print()