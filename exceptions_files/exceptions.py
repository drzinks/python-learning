with open("testfile2.txt","w") as testfile2:
    testfile2.write("First line\n")
    #0/0
    testfile2.write("This line will never be written if 0/0 is present")