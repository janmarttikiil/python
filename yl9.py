a = float(input("mis on kolmnurga esimene: "))
b = float(input("mis on kolmnurga teine: "))
c = float(input("mis on kolmnurga kolmas: "))

if a+b<c or c+b<a or a+c<b:
    print("selline kolmnurk ei saa eksisteerida")
elif a==b==c:
    print("see kolmnurk on võrdkülgne")
elif a==b or a==c or b==c:
    print("see kolmnurk on võrdhaarne")
else:
    print("see kolmnurk on erikülgne")