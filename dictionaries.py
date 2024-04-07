mydict = {"name": "Max", "age": 28, "city": "New York"}
# you can add and change

value = mydict["name"]
print(value)

mydict["email"] = "cool@xyz"
print(mydict)

del mydict["name"]
print(mydict)

for key in mydict.keys():
    print(key)

#effective copy
mydict_copy = mydict.copy()#to protect original one

mydict2 = {"name": "Marry", "age": 22, "city": "New York"}
mydict.update(mydict2)
print(mydict)

