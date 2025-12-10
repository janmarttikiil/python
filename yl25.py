dict={
    "first_name": "jan-martti",
    "last_name": "Kiil",
    "birth_year": 2009,
    "location": "Eesti",
    "favorite_treat": "kummikarud",
}

print(dict.get("location"))
print(dict["location"])
print(dict.update({"favorite_treat": "hapu kummikarud"}))
print(dict.keys())
print(dict.values())

if "isikukood" in dict:
    print("isiku kood on olemas")
else:
    print("isiku kood puudub")

print(len(dict))

dict["length"]=172
dict.pop("birth_year")
del dict["birth_year"]