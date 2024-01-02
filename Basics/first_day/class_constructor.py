

    # init method acts as the constructor
    
class Employee:
    
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        
    def employee_details(self):
        print("name of the employee", self.name)
        print("age of person", self.age) 
        print("salary" ,self.salary)
        print("gender is",self.gender)
        
e1 = Employee("abd",12,1000,"Male")  
e1.employee_details()        