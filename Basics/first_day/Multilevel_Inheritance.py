'''
Multilevel:
parent,child,grand-child


'''


class Parent:
    def assign_name(self,name):
        self.name=name

    def show_name(self):
        return self.name
    
class Child(Parent):
    def assign_age(self,age):
        self.age=age
        
    def show_age(self):
        return self.age
    
class GrandChild(Child):
    def assign_gender(self,gender):
        self.gender=gender
        
    def show_gender(self):
        return self.gender
    
g1 = GrandChild()
g1.assign_name("anne")
g1.assign_age(10)
g1.assign_gender("M")
g1.show_name()
g1.show_age()
g1.show_gender()


