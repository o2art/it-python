#tekst = "PNRFSRLTKOALPZNUZCEAPOEOBIETNJESYACYIL"
method = input("s- szyfrowanie, d - deszyfrowanie: ")
if method == "d":
    tekst = input("Podaj zaszyfrowany tekst: ")

    tab = [[], []]
    odp = ""
    x = len(tekst)
    y = int(x/2)

    for i in range(y):
        tab[0] += tekst[i]

    for i in range(y):
        tab[1] += tekst[i+y]

    print(tab[0])
    print(tab[1])

    for i in range(len(tab[0])):
        for t in range(len(tab)):
            if t == 0:
                odp += tab[t][i]
            else:
                odp += tab[t][i]

    print("\n" + odp)
else:
    #tekst = "WLASNE MALE OGNISKO CENNIEJSZE OD STOSU ZLOTA"
    tekst = input("Podaj tekst do zaszyfrowania: ")

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
