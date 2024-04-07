# multiplication
result = 7 * 5
print(result)

# power operation
result = 2 ** 4
print(result)

# list
zeros = [0] * 10
onetwos = [1, 2] * 5
print(zeros)
print(onetwos)

#------------------
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
my_function("Hey", 3, [0, 1, 2], name="Alex", age=8)

def my_function2(name, *, age):
    print(name)
    print(age)

# my_function2("Michael", 5) --> this would raise a TypeError
my_function2("Michael", age=5)

#unpacking ---------------
numbers = (1, 2, 3, 4, 5, 6, 7, 8)

*beginning, last = numbers
print(beginning)
print(last)

print()

first, *end = numbers
print(first)
print(end)

print()
first, *middle, last = numbers
print(first)
print(middle)
print(last)