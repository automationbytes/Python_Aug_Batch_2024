with open("example.txt", "a+") as file:
    file.write("Hello World")
    file.seek(0)
    print(file.read())


    '''
    r+ - read and write. throws exception when file is not found. it will preserve
    w+ - read and write. it will overwrite
    a+ - read and write - will create a new file when the file is not found
    '''