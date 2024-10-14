with open("imionanazwiska.txt", "r", encoding="UTF-8") as imionanazwiska_file:
    list_name_surname = []
    for line in imionanazwiska_file:
        temp_line_array = line.replace("\n", "").split(" ")
        if (len(temp_line_array) == 2):
            list_name_surname.append((temp_line_array[0], temp_line_array[1]))
            # print((temp_line_array[0], temp_line_array[1]))
    print(list_name_surname)

    with open("imiona.txt", "w", encoding="UTF-8") as imiona_file:
        for name, surname in list_name_surname:
            imiona_file.write(name + "\n")
        print(name)
    with open("nazwiska.txt", "w", encoding="UTF-8") as nazwiska_file:
        for name, surname in list_name_surname:
            nazwiska_file.write(surname + "\n")
        print(surname)
