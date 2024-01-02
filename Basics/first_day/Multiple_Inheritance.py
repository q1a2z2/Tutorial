'''
Single
MULTIPLE
Multilevel
Hybrid
'''

'''
MULTIPLE:
class one, class two, child class
'''

class Parent1:
    def assign_str(self,str1):
        self.str1 = str1
        
    def show_str1(self):
        print(self.str1)
        
class Parent2:
    def assign_str2(self,str2):
        self.str2 = str2
        
    def show_str2(self):
        print(self.str2)
        

class Child(Parent1,Parent2):
    def assign_str3(self,str3):
        self.str3 = str3
        
    def show_str3(self):
        print(self.str3)
        
c1 = Child()
c1.assign_str("sparta")
c1.assign_str2("This is sparta")
c1.assign_str3("Hello World")

c1.show_str1()
c1.show_str2()
c1.show_str3()
                   