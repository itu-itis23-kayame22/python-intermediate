#Tuples can't change after creation

mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

for i in mytuple:
    print(i)

newtuple = ('a', 'p', 'p', 'l', 'e',)
print(newtuple.count('p'))

a = (1, 2, 3, 4, 5, 6, 7)
b = a[::1] #go all way with step 1

name, age, city = mytuple
print(name)# packing the tuple
print(age)

#tuples are fast than lists and cover less memory