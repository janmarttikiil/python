name=input("mis on sinu nimi: ")
print("Tere, ",name)
elukoht=input("kus sa elad: ")
if elukoht==("saaremaal") or elukoht==("Saaremaal"):
    print("Mina elan ka Saaremaal")
age=int(input("kui vana sa oled: "))
if age < 18:
    print("sa oled liiga noor, et autoga sõita")
elif age==18:
    print("palju õnne täisealise saamise puhul")
else:
    print("sina oled täiselaine sina võid autoga sõita")