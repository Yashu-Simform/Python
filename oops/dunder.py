class Equipment:
    __total_eqip = 0
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
        pass

    def get_details(self):
        print(self.name, self.quantity,sep=' ')


    #Operator Overloading or Magic Methods Overriding
    def __add__(self, other):
        return (self.price * self.quantity + other.price * other.quantity)

    def __len__(self):
        return self.quantity


hammer = Equipment("Hammer", 5, 120)
screw = Equipment("Screw", 50, 5)

print('Total Price: ', (hammer + screw))

print('Total Quantity: ', len(hammer))