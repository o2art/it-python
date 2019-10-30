MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

choice = input("s - szyfrowanie, d - deszyfrowanie \n")

if(choice == "s"):
    message = input("tekst do szyfrowania: ")
    out = ''
    for i in message:
        if i != " ":
            out += MORSE_CODE_DICT[i.upper()] + " "
        else:
            out += " "
    print(out)
elif(choice == "d"):
    message = input("tekst do deszyfrowania: ")
    out = ''
    outer = ''
    for i in message:
        if i != " ":
            l = 0
            out += i
        else:
            l += 1
            if l == 2:
                outer += " "
            else:
                outer += list(MORSE_CODE_DICT.keys()
                              )[list(MORSE_CODE_DICT .values()).index(out)]
                out = ''
    print(outer)
else:
    print("podałeś złą opcję :--(((")
