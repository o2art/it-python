tekst = "UCZCIWOSC ZBIERA POCHWALY I UMIERA Z ZIMNA"

tab = [[],[],[],[]]
key = [3, 2, 0, 1]
x = 0
odp = ""

for i in tekst:
    if i == " ":
        continue
    else:
        tab[x].append(i)
        x+=1
        if x == 4:
            x = 0

for i in range(4):
    print(tab[i])

x = 0
for i in range(len(tab)):
    for y in range(len(tab[key[x]])):
        odp += tab[key[x]][y]
    x+=1

print("\n" + odp)