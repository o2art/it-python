coded = "SF SFZPJ SNLID SNJ OJXY EF UTEST"
decoded = []
for i in range(len(coded)):
    if (coded[i] >= 'A' and coded[i] <= 'Z'):
        decoded.append(chr(65 + (ord(coded[i]) - 18) % 26))
    else:
        decoded.append(" ")

out = ''.join(decoded)
print(out)
