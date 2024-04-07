def print_name(name): # parameter
    print(name)

print_name('Alex') # argument

def foo(a, b, c):
    print(a, b, c)
    
foo(1, 2, 3)

foo(a=1, b=2, c=3)
foo(c=3, b=2, a=1) # order is not important here
# mix of both
foo(1, b=2, c=3)


def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

# 3, 4, 5 are combined into args
# six and seven are combined into kwargs
foo(1, 2, 3, 4, 5, six=6, seven=7)
print()

#unpacking -----------------
def foo(a, b, c):
    print(a, b, c)

my_list = [4, 5, 6] # length must match
foo(*my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)

# my_dict = {'a': 1, 'b': 2, 'd': 3} # not possible 

# local and global vars -----------------------------
def foo1():
    x = number 
    print('number in function:', x)

number = 0
foo1()

# modifying the global variable
def foo2():
    global number 
    number = 3

print('number before foo2(): ', number)
foo2() # modifies the global variable
print('number after foo2(): ', number)