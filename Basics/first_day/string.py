from re import MULTILINE

s1 = "Hello world"
print(type(s1))


#multiline string

s1 = ''' this is MULTILINE
string'''
print(s1)


my_string = "My name is john, john"
print(my_string[-1])

print(my_string[3:7])
#output name

print(my_string[11:15])
#output john

#find len of str
print(len(my_string))

print(my_string.lower())
print(my_string.upper())

#replace
print(my_string.replace('n', 'y'))

#ocurence
print(my_string.count('john'))

#find index
print(my_string.find('john'))

#split
print(my_string.split(','))





