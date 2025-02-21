class BankMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Bank(metaclass=BankMeta):
    pass




if __name__ == "__main__":
    # The client code.

    o1 = Bank()
    o2 = Bank()

    print(id(o1))
    print(id(o2))

    if id(o1) == id(o2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")