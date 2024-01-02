'''
class Phone:
    
    def make_call(self):   #self is referencing class
        print("make call")
        
    def play_game(self):
        print("play game")
        
p1= Phone()  #initiating object

p1.make_call()
p1.play_game()   
 '''   

    
    
    
    #********** Adding Parameter TO class**************
 '''   
 class Phone:
    def set_color(self,color):
        self.color = color
        
    def set_cost(self,cost):
        self.cost = cost
    
    def mobile_color(self):
        return self.color
 
    def cost_mobile(self):
        return self.cost
    
    def make_call(self):
        print("Make calls")
        
    def play_game(self):
        print("Play games")
    
p1 = Phone()
p1.set_color("Blue")
p1.set_cost(10000)
p1.mobile_color()
p1.cost_mobile()
'''







        
        
        

