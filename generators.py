#Generators are functions that can be paused and resumed on the fly

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(3)# activate

print(next(cd))# first value
print(next(cd))# second
print(next(cd))# third

#print(next(cd))# this will raise a StopIteration

#COMPPARE MEMORY USAGE

# without a generator 
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")

# with a generator
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")

#----------------

# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))