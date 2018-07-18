
with open("data/data.txt", "r+") as fo:
    fo.seek(5)                  #seek method moves the cursor to a specific place in the file
    # str = fo.read(5)
    # str2 = fo.read(10)
    # print(str + str2)
    fo.write("STEINNNN")
    print(fo.tell())
    
