alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alTab = []

keyIn = "NIKT NIE JEST BEZ WAD"
keyOut = []

for i in range(len(keyIn)):
    if keyIn[i].lower() not in keyOut and keyIn[i] != " ":
        keyOut.append(keyIn[i].lower())

print(keyOut)
for i in range(len(keyOut)):
    alTab.append([])
    for k in range(len(alfabet)):
        alTab[i].append(
            chr(65 + (ord(keyOut[i]) + ord(alfabet[k]) - 6) % len(alfabet)))
    print("Tab", i, ":", alTab[i])

decipher = "GENIUSZ TO TYLKO SPRAWA CIERPLIWOSCI"
cipher = []
k = 0

for i in range(len(decipher)):
    if(decipher[i] == " "):
        cipher.append(" ")
    else:
        if(k == len(keyOut)):
            k = 0
        cipher.append(
            alTab[k][alfabet.index(decipher[i].upper())])
        k += 1

out = ''.join(cipher)
print("Szyfr: ", out)
