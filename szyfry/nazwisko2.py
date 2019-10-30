import math

tekst = input("Podaj zaszyfrowany tekst: ")
dlugosc = input("Podaj ilosc kolumn: ")

tab = []
key = []
XD = 0

print("Podaj kolejne wartosci klucza: \n")

while XD < int(dlugosc):
    tab.append([])
    x = input()
    key.append(int(x))
    XD += 1

x = len(tekst) % len(key)
y = math.floor((len(tekst) - x) / len(key))
i = 0
xD = 0

print("\n")

for a in tekst:
    if xD == y and key[i] > x - 1:
        i += 1
        xD = 0
    elif xD == y + 1:
        i += 1
        xD = 0
    tab[key[i]].append(a)
    xD += 1

i = 0
xD = 0
koniec = ""

for x in range(len(tekst)):
    if i == len(key):
        i = 0
        xD += 1
    koniec += tab[i][xD]
    i += 1

print("Wynik: " + koniec)