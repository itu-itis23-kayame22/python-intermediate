# arguments: expression
add10 = lambda x: x+10
print(add10(5))

mult = lambda x,y: x*y
print(mult(2, 7))

points2D = [(1, 2), (15, 1), (5, -1),(10, 4)]
p_sort = sorted(points2D, key=lambda x: x[1])# sort respect to y
print(p_sort)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))
c = filter(lambda x: x%2==0, a)
print(list(c))

