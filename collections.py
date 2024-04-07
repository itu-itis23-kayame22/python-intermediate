# counter, namedtuple, ordereddict, defaultdict, deque
from collections import Counter
a = "aaaaabbbbcc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))

from collections import namedtuple
point = namedtuple('point', 'x,y')
pt = point(1, -4)
print(pt.x, pt.y)

from collections import OrderedDict
dict = OrderedDict()
dict['a'] = 1
dict['c'] = 3
dict['b'] = 2

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])


from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.extend([4,5,6])
print(d)

