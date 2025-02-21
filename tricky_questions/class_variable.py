class A:
    v = [1222]

    def update(self, x):
        A.v = x
        #!WARNING : self.v = x  Again a re-assignment operation will create a new varaible in instance namespace

o1 = A()
o2 = A()
print(f'Memory address of o1.v {id(o1.v)}')
print(f'Memory address of o2.v before re-assignment {id(o2.v)}')
o2.v = [1222]
print(f'Memory address of o2.v after re-assignment {id(o2.v)}')
print(f'Memory address of A.v {id(A.v)}')