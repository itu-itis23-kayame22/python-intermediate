#unordered, mutable, no duplicate
myset = {1, 2, 3, 1}
print(myset)

myset.add(4)
print(myset)

odds = {1, 3, 5, 7}
evens = {0, 2, 4, 6}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = primes.intersection(evens)
print(i)

# changes and assigments won't modify
u.update(primes) # to really update

print(i.issubset(u))#to check subset or not
print(i.issuperset(u))#to check superset or not
print(i.isdisjoint(u))#to check no coomon value







