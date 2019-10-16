coded = "KLAMSTWO MA KROTKIE NOGI"
decoded = []
for i in range(len(coded)):
    if (coded[i] >= 'A' and coded[i] <= 'Z'):
        decoded.append(chr(65 + (ord(coded[i]) - 4) % 26))
    else:
        decoded.append(" ")

out = ''.join(decoded)
print(out)
