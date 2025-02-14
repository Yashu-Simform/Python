a = [2,3,4,5]
b = 2


a_itr = a.__iter__()
print(next(a_itr))
print(next(a_itr))
print(next(a_itr))
print(next(a_itr))
# print(next(a_itr))  # Raise an error of StopIteration

st = 'Elephant'
stitr = st.__iter__()

print(next(stitr))
print(next(stitr))


class MyIterables:
    def __init__(self, iterable):
        self.iterable = iterable
        self.indx = 0
        self.end = len(iterable)
        pass


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indx > self.end:
            raise StopIteration
        
        self.indx += 1
        return self.iterable[self.indx-1]


myitr = MyIterables([45,56,67,78,89])
print(next(myitr))
print(myitr.__next__())
print(myitr.__next__())
print(myitr.__next__())
print(myitr.__next__())


# Create an iterator such that it iterate through words in string.
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.indx = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.indx > len(self.words):
            raise StopIteration
        self.indx += 1
        return self.words[self.indx-1]




#------------------Generators------------------------------
def cube_it(*args):
    output = []
    for i in args:
        output.append(i*i*i)

    return output


def cube_it_gen(*args):
    for i in args:
        yield i*i*i


print(cube_it(*[1,2,3,4,5,6,7,8,9]))

gentr = cube_it_gen(*[1,2,3,4,5,6,7,8,9])
print(gentr)
for i in gentr:
    print(i)



#How to access value in python if we have memory address
import ctypes
for i in a:
    ad = id(i)
    getval = ctypes.cast(ad, ctypes.py_object).value
    # print(getval)