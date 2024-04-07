mylist = ["banana", "cherry", "apple"]
print(mylist)
item = mylist[1] #cherry

#list can contain different data types

for i in mylist:
    print(i)

if "banana" in mylist:
    print("yes")
else:
    print("no")

mylist.insert(1, "blueberry") #adding spesific index
mylist.remove("banana")

newlist = [0] * 5
print(newlist) # to print 5 zero

sum_list = newlist + mylist #to merge

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
a = num_list[2:5] #to cut spesific part

mylist_copy = mylist # changes will affect both list
mylist_copy = mylist.copy() # use this instead

#Comprehension
b = [i*i for i in num_list]


