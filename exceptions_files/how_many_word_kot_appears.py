def how_many_word_appears_in_file(filename, word):
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            return file.read().count(word)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You don't have permissions to open the file.")

while(True):
    filename = input("Type file name to be sarched: ")
    word = input("\nType word, you want to check how many: ")

    count = how_many_word_appears_in_file(filename,word)

    if(count is not None):
        print(f"The word {word} appears in file {filename} {count} times.")