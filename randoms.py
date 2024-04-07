import random

a = random.random()
print(a)
a = random.uniform(1,10)# if range [a,b]
print(a)
a = random.randint(1,10)#for int
print(a)
a = random.choice(list("ABCDEFGHI"))#for letters
print(a)
# shuffle list
a = list("ABCDEFGHI")
random.shuffle(a)
print(a)

#Seeding 
print('Seeding with 1...\n')

random.seed(1)
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

#Secrets
import secrets

a = secrets.randbelow(10) #random int below 10 to zero
print(a)
a = secrets.randbits(5) #random int with 5 bit
print(a)
a = secrets.choice(list("ABCDEFGHI"))
print(a)

