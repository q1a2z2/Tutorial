'''
a = 10
b = 20

if a>b:
    print("A is greater than B")

else:
    print("a is not greater than b")
'''
'''
a = 10
b = 20
c = 30

if (a>b & a>c):
    print("a is greater")
    
elif (b>a & b>c):
    print("b is greater")
    
else:
    print("C is greater")
 '''   
'''   
tuple = (1,2,3,4)
if 2 in tuple:
    print("2 is present")
'''

l1 = [1,2,3,4]
if l1[1]==2:
    l1[1]=l1[1]+100
    print(l1) 
    

l2 = [1,2,3,4]
if l2[3]==5:
    l2[3]=l2[3]+100 
else:
    l2[3]=l2[3]+500
    print(l2)
    
#if with dict

d1 = {"a":1,"b":2,"c":3}
if d1["b"]==2:
    d1["b"]=d1["b"]+100
    print(d1)


