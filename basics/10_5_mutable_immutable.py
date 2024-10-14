import copy
myList = [[1,2],[3,4],[5,6]]
print(myList)
myList2 = copy.deepcopy(myList)
myList2[0][0] = 0
print(myList)
print(myList2)

