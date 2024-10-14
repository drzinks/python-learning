with open("oceany.txt", "r", encoding="UTF-8") as oceany_file:
    # for line in oceany_file:
    #     print(line)
    print(oceany_file.readline())
    print(oceany_file.tell())  #gdzie jest kursor 12
    print(oceany_file.readline())
    print(oceany_file.tell())  #gdzie jest kursor 22
    oceany_file.seek(0) #przestaw kursor na 0
    print(oceany_file.readline())

with open("oceany.txt", "a", encoding="UTF-8") as oceany_file:
    print(oceany_file.tell())
    oceany_file.write("append to end")