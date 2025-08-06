list1=[12,89,78,90]
list2=["suhaib","raju","python"]
list3="suhaib"
list1.extend(list2)
#print(list1)
list1.extend(list3)
#it will append list3 character by character

#like   's','u',h',a','i','b'
print(list1)


#pop method

list1.pop()
print(list1)

list2.pop()
print(list2)

list1.pop(1)
print(list1)

#in order to remove     list1.remove("suhaib")
list2.remove("suhaib")
print(list2)

list1.remove(90)
print(list1)



