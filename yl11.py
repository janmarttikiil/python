string = input("Sisesta string: ")

cleaned_string = string.strip()

if len(cleaned_string) >= 7 and len(cleaned_string) % 2 == 1:
    middle_index = len(cleaned_string) // 2
    print("Kolm keskmist sümbolit:", cleaned_is [middle_index - 1 : middle_index + 2])
else:
    print("String ei vasta tingimustele!")
