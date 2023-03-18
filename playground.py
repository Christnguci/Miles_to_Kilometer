def add (**number):
    sum=0
    for n in number :
        sum+=n
    
    return sum

def calculate(**kwargs) :
    print(kwargs)
    print(kwargs.get("add"))

calculate(add=3, multiply=5)

class Car:
    def __init__(self,**kw):
        self.make=kw["make"]
        self.model=kw["model"]
    def name_car(self):
        print(self.make)
        print(self.model)

mycar=Car(make="Nissan",model="GTR")
mycar.name_car()