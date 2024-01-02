#List: list are mutable

#changing element

l1 = [1,'a',True,2,'b',False]
l1[2] = 'c'
print(l1)

#add element
#l1.append('')

#Pop element
l1.pop(1)
print(l1)

#Reverse a list
l1.reverse()
print(l1)

l2 = ['mango', 'apple','bannana','berry']
l2.sort()
print(l2)
l2.insert(1, 'sparta')
print(l2)

#concat
print(l1 + l2)



