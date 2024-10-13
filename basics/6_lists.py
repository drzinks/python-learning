names = ["Michal", "Maciej", "Piotrek", "Patryk", "Jaroslaw"] #indexed from 0
numbers = [1,2,3,4]
mixed = [1,"aa",52,"kk"]


#for name in names:
    #print(name)

print(names[-2])
names[-2] = "Wojciech"

for name in names:
    print(name)

print("Maciej" in names) #True

if("Maciej" in names):
    print("Hej Maciek!")

#not in

mixed += names

for e in mixed:
    print(e)

