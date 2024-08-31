'''

File Handling -
read = r
write = w
append = a
create = x
close
delete


'''
#
# file1 = open("sample.txt","w")
# file1.write("Hello")
# #
# f = open("sample.txt","r")
# print(f.readline())
#



with open("sample.txt","w") as f:
    f.write("Hello World \n")
    li = ["Python supports two types of comments: \n", "1) Single Line Comment \n", "2) Multi Line Comment"]
    f.writelines(li)

with open("sample.txt","r") as f:
    print(f.read())


f = open("sample.txt","a")
f.write("Hello World second time \n")
f.close()


with open("sample.txt","r") as f:
    print(f.read())

