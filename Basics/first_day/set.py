

#Set: unordered and unindexced collection of elements. Duplicates are not allowed

s1 = {1,"sparta"}

#add new element
s1.add("hello")
print(s1)
#it prints according to alphaaetical order
#output:1,hello,sparta

#remove element
s1.remove(1)
print(s1)

#update element with another set
s2={2,1,"abc"}
s1.update(s2)
print(s1)

#union(concat)
#intersection(common elements
s3 = {1,2,3,4,}
s4={5,6,7,4}
s3.intersection(s4)
print(s3)