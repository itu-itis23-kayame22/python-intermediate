# ordered, immutable
mystring = "hello"
multi_line = """
   hello
   world
"""
print(mystring)
print(multi_line)

substring = mystring[2:4]
print(substring)

new_string = multi_line.strip()
print(new_string) #to eliminate space

print(mystring.startswith("hel"))#to check characters

print(mystring.replace("hello","hi"))

text = "my name is fatih"
new_text = text.split()
print(new_text)

mylist = ['a'] * 6
new2 = ''.join(mylist)#much faster than for loop
print(new2)

var = 6
my_new = f"the variable: {var}"
print(my_new)


 

