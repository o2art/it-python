alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alTab = []

keyIn = "KRYPTOLOGIA"
keyOut = []

for i in range(len(keyIn)):
    if keyIn[i].lower() not in keyOut and keyIn[i] != " ":
        keyOut.append(keyIn[i].lower())

print(keyOut)

for i in range(len(keyOut)):
    keyOut[i] = chr(
        65 + (26 - alfabet.index(keyOut[i].upper())) % 26).lower()

print(keyOut)

for i in range(len(keyOut)):
    alTab.append([])
    for k in range(len(alfabet)):
        alTab[i].append(
            chr(65 + (ord(keyOut[i]) + ord(alfabet[k]) - 6) % len(alfabet)))
    print("Tab", i, ":", alTab[i])

cipher = "QEGTP XPYB PBRECBSYOMM ZFKHSQKKVIK BPORKOE"
decipher = []
k = 0

for i in range(len(cipher)):
    if(cipher[i] == " "):
        decipher.append(" ")
    else:
        if(k == len(keyOut)):
            k = 0
        decipher.append(
            alTab[k][alfabet.index(cipher[i])])
        k += 1

out = ''.join(decipher)
print("Tekst jawny: ", out)
