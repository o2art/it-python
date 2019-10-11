tekst = "WLASNE MALE OGNISKO CENNIEJSZE OD STOSU ZLOTA"

tab = [[],[]]
odp = ""
x = len(tekst)
key = True

for i in range(x):
    if tekst[i] != " ":
        if key == True:
            tab[0].append(tekst[i])
            key = False
        else:
            tab[1].append(tekst[i])
            key = True

print(tab[0])
print(tab[1])

for i in range(len(tab[0])):
        odp += tab[0][i]

for i in range(len(tab[1])):
    odp += tab[1][i]

print("\n" + odp)