import random
choices = ["kivi", "paber", "käärid"]

while True:
    user_choice=input("sisesta kivi, paber, käärid või välju et mängu lõppetada ").lower() 
    if user_choice == "välju":
        print("mäng on lõppenud")
        break
    if user_choice not in choices:
        print("kontrolli üle mida sa kirjutasid")
        continue

    computer_choice=random.choice(choices)
    print("arvuti valis", computer_choice)
    if user_choice==computer_choice:
        print("viik!")
    elif (user_choice == "kivi" and computer_choice == "käärid") or (user_choice == "paber" and computer_choice == "kivi") or (user_choice == "käärid" and computer_choice == "paber"):
        print("sina võitsid")
    else:
        print("sina kaotasid")