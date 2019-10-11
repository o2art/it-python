tekst = "BZOIJPYECYNSNEAEDOZNUZNCDOCK"

tab = [[],[],[]]
odp = ""
x = len(tekst)
y = int(x/2)
z = int(y/2)

for i in range(z):
    tab[0] += tekst[i]

for i in range(y):
    tab[1] += tekst[i+z]

for i in range(z):
    tab[2] += tekst[i+y+z]

for i in range(len(tab[0])):
    for t in range(len(tab)):
        if t == 2:
            odp += tab[t][i]
            if i == 0:
                odp += tab[1][1]
            elif i*2+1 <= len(tab[1]):
                odp += tab[1][(i*2)+1]
        elif t == 1:
            odp += tab[t][i*2]
        else:
            odp += tab[t][i]

print("\n" + odp)
