class Vehicle:
    def __init__(self, name, category, price, owner):
        self.name = name
        self.category = category
        self.price = price
        self.owner = owner
        self.det = self.owner + '-' + self.name
        pass


#   ---------------- Getter ---------------------
    # Implicitly call getter method when attribute is accessed if getter is not defined explicitly
    @property
    def det(self):
        if (not self.name) or (not self.name):
            return None
        return self.owner + '-' + self.name
    

    #If getter is explicitly defined for any attribute it will be called when attribute is accessed.
    @det.getter        
    def det(self):
        return self.owner


#   -------------- Setter -----------------------
    @det.setter
    def det(self, detail):
        if detail:
            owner, carname = detail.split('-')
            self.name = carname
            self.owner = owner


#   ------------- Deleter ------------------------
    @det.deleter
    def det(self):
        self.name = None
        self.owner = None
        self.price = None
        self.category = None

        print('This Object is deleted!')


car = Vehicle("Maruti SUZUKI", "car", 400000, "Dahood")

print(car.det)

car.det = 'Dahood-Tata Nano'

print(car.det)

del car.det