list = ["õun", "banaan", "mandariin"]
print(list[0])
list.append("mango")
print(list)
print(list[3])
list[1] = ("apelsiin")
print(list)
if "õun" in list:
    print("Õun on listis!")
else:
    print("Õuna ei ole listis.")
print(len(list))
list.remove("mango")
print(list)
list.reverse()
print(list)
list.sort()
print(list)