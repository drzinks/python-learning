try:
    testfile = open("testfile.txt", "w")  # file handle
    testfile.write("szpadyzor\n")
    #0 / 0
    testfile.write("szpadyzor")
    testfile.write("szpadyzor")
finally:
    testfile.close()
