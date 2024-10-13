tuple1 = 1,42,3,4, "abc"
print(tuple1[-1])
#dictionaries
rooms = {49: "Michał Gołębiowski", 69: "Maciej Buczek"}
print(rooms)
#sets
set1 = {1,2,3,4}
print(set1)
list2=[1,1,1,1,3,6]
set2 = set(list2) #removes duplicates
print(set1&set2)
print(set1|set2)
set1
#{1, 2, 3, 4, -1}
set2
#{1, 3, 6}
print(set1-set2)
#{2, 4, -1}
print(set1^set2)
#{2, 4, 6, -1}
guestList = [
        ["Michał Gołębiowski", 42, "male"],
        ["Maciej Buczek", 43, "male"],
        ["Agata Krzyżanowska", 38, "female"]
    ]
for name, age, gender in guestList:
    print("Name: ", name)
    print("Age: ", age)
    print("Gender: ", gender) 
    print("\n")
