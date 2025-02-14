class A:
    def __init__(self, name):
        self.name = name
        pass

    def printD(self):
        print(self.name)


class B(A):
    def __init__(self, surname):
        self.surname = surname
        pass

    def printD(self):
        print(self.surname)


class C(A):
    def __init__(self, home):
        self.home = home
        pass

    def printD(self):
        print(self.home)


class D(B,C):
    def __init__(self, **details):
        self.contact = details['contact']
        B.__init__(self, details['surname'])
        C.__init__(self, details['home'])
        A.__init__(self, details['name'])
        pass

    def printD(self):
        #2 ways to access the methods of parents in multiple inheritance.
        B.printD(self)
        C.printD(self)
        A.printD(self)
        print(self.contact)


objD = D(name="Yashu", surname='Ranparia', home='Junagadh', contact='1234567890')
objD.printD()