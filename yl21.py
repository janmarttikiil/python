import random
n = random.randint(1, 100)
guess = None
while guess != n:
    guess = int(input("Arva ära number vahemikus 1-100: "))
    if guess < n:
        print("Liiga väike!")
    elif guess > n:
        print("Liiga suur!")
    else:
        print("Õige! Number oli", n)