slang_miejski = {}
while(True):
    decision = input("Add(a), Search(s) or exit(e)");
    if decision == "e":
        break
    elif decision == "a":
        word = input("Give the word: ")
        description = input("Give the description: ")
        slang_miejski.update({word:description})
        print("dictionary updated")
    elif decision == "s":
        search_term = input("Give the search term: ")
        if search_term in slang_miejski:
            description = slang_miejski.get(search_term)
            print("Description is: \n", description)
        else:
            print("Term not found)
    print("Whole dictionary \"slang miejski\":\n", slang_miejski)
