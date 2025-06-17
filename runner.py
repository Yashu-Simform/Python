# def fun():
#     value = yield 4

#     print(value)

#     yield (value * 10)


# a = fun()
# print(next(a))

# print(a.send(5))


# class A:
#     v = [1222]

#     def update(self, x):
#         A.v = x
#         #!WARNING : self.v = x  Again a re-assignment

#     @staticmethod
#     def statFun():
#         print('Its a static one!')

# o1 = A()
# o2 = A()

# # A.statFun()
# print(dir(o1))


#---------------------------- Generators--------------------------------------
# def funcx():
#     name = "Main"
#     var1 = yield name
#     print(var1)

# gen_obj = funcx()
# print(type(gen_obj)) # must be of type generator object

# Must be primed

# print((next(gen_obj))) # Must returned name variable inside of funcx

# gen_obj.send('10') #Print('10') inside the funcx

# Generator Expression
# gen_obj = (i for i in range(10))
# print(type(gen_obj))


# File Handling
# import json
# adict = [{'a': 1}, {'b': 2}, {'c': 3}]

# with open('data.json', 'w') as f2:
#     json.dump(adict, f2)