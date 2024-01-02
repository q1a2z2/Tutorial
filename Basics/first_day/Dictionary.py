

#Dictionary: Dictionary is mutable, unordered collection whereas list and tuple are ordered collection

fruit = {"Apple":10,"Orange":20,"Peaches":100,"Bannana":30}
print(type(fruit))

#here keys are apple,orange etc
#values are 10,20,100

#extracting keys

#fruit.keys()
#print(fruit)
#values
#fruit.values()
#print(fruit)

#extracting item
fruit.items()
print(fruit)

#adding new element
fruit["Mango"] = 50
print(fruit)

fruit["Apple"] =15
print(fruit)

#update first dictionary with another
fruit1 = {"mango":10}
fruit2={"guave":45,"kaka":12}
fruit1.update(fruit2)