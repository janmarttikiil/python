a = int(input("siseta aasta number: "))

if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
    print("aasta on liigaasta")
else:
    print("aasta on lihtaasta")