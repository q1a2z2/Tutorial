# one class derived the properties of another class


class Vehicle:
    
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
        
    def show_details(self):
        print("I am the vehicle")
        print("Mileage of the car:",self.mileage)
        print("Cost of the car:",self.cost)
        
        
#v1 = Vehicle(500,500)
#v1.show_details()
    
class Car(Vehicle):    #child class

#overiding init method
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp = hp
    
    
    def show_car_details(self):
        print("Im the car")
        print("Tyres range",self.tyres)
        print("hp of car",self.hp)
        
c1 = Car(100,2000,150,1000)
c1.show_details()    
c1.show_car_details()

