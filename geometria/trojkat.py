a = int(input("podaj bok a: "))
b = int(input("podaj bok b: "))
c = int(input("podaj bok c: "))

if(a < 0 or b < 0 or c < 0):
    print("podałeś złą długość")
else:
    if(a+b > c and a+c > b and b+c > a):
        if(a**2+b**2 == c**2 or a**2+b**2 == c**2 or b**2+c**2 == a**2):
            print("trójkąt prostokątny")
        else:
            print("da się")
    else:
        print("nie da się")
