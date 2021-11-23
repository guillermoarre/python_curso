#Lista anidadas
list1=[1,2,3,[True,False,"Python"]]
#print(list1[3][2])

#Append
#Agregar un solo valor a la lista al final de esta
list2 = [1,2,3,4]
list2.append("hello")

#Extend
list2.extend([10,11,True,'python'])
#print(list2)

#Insert
list2.insert(1,'test')
print(list2)

#Remove
list2.remove(2)
print(list2)

#Pop
list2.pop(2)
print(list2)


