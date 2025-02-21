# def fun():
#     value = yield 4

#     print(value)

#     yield (value * 10)


# a = fun()
# print(next(a))

# print(a.send(5))


class A:
    v = [1222]

    def update(self, x):
        A.v = x
        #!WARNING : self.v = x  Again a re-assignment

    @staticmethod
    def statFun():
        print('Its a static one!')

o1 = A()
o2 = A()

# A.statFun()
print(dir(o1))