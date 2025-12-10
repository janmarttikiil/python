text=input("Sisesta tekst: ")

vowels="aeiouõäöüAEIOUÕÄÖÜ"

count=0

for char in text:
    if char in vowels:
        count += 1

print("Selles tekstis on ", count, "täishäälikut.")