list = ["Michal","Maciej"]
list2 = ["Michal","Maciej"]
list.append(["Miron","Marcin"])
#appends a single object, list of lists ['Michal', 'Maciej', ['Miron', 'Marcin']]
print(list)
print("############")
list2.extend(["Miron","Marcin"])
print(list2)
#['Michal', 'Maciej', 'Miron', 'Marcin']
list2.insert(2,"Jaroslaw") 
print(list2)
print(list2.index("Miron"))
print(list2)
list2.sort()
print(list2)
list3 = [1,2,3,4,-55]
print(min(list3))
#.append - add (uwaga: może być lista list)
#.extend - rozszerzyć
#min(list)
print(list2.count("Miron"))
#pop - removes last element
#remove - removes first occurence
print(list2)
#['Jaroslaw', 'Maciej', 'Marcin', 'Michal', 'Miron']
list2.pop()
print(list2)
#['Jaroslaw', 'Maciej', 'Marcin', 'Michal']
list2.remove("Jaroslaw")
print(list2)
#['Maciej', 'Marcin', 'Michal']
list2.reverse()
print(list2)
#['Michal', 'Marcin', 'Maciej']
list2.clear()
print(list2)
