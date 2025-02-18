from collections import Counter, namedtuple, OrderedDict, deque, defaultdict

astr = 'abcaabc'
alst = ['1', '2', '3', '1', '5']


def use_counter():
    cntr = Counter([1,3,1,2,4,5,4,4])

    print(cntr.items())
    print(cntr.most_common(1))
    for i in cntr.elements():
        print(i)

def use_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    pt = Point(2,3)
    print(pt.x, pt.y)
    pass


def use_ordereddict():
    b = OrderedDict()
    b[2] = 2
    b[1] = 1
    b[3] = 3
    b[4] = 4

    b.move_to_end(4, last=False) #Move the specified key to last or first 
    pass

def use_deque():
    q = deque([1,2,3,4,5,6,7,8,9])

    q.append(10)
    q.appendleft(0)
    print(q)
    q.pop()
    q.popleft()
    print(q)
    q.extend([11,12,13])
    q.extendleft([-1,-2,-3])    # Extends the deque by adding the given iterable in reverse order
    print(q)


def use_defaultdict():
    ddict = defaultdict(str)
    ddict[1] = 2
    ddict[2] = 'b'

    print(ddict)
    print(ddict[3])

# use_counter()
# use_namedtuple()
# use_deque()
use_defaultdict()