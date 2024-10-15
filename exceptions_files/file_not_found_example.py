
def get_file_content(filename):
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print("File does not exist.")

while(True):
    filename = input("Type filename to open: ")
    if(filename == 'x'):
        break
    print(get_file_content(filename))