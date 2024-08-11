#start - init, stop- condition, step- increment
for i in range(1,10,1):
    print(i)
print("*****************")

for i in range(10,101,10):
    print(i)
print("*****************")

# if step is not provided by default; step will be defaulted to 1
for i in range(5,50):
    print(i)
print("*****************")

# if start is not provided by default start will b 0
for i in range(50):
    print(i)

a= 5
b = 10
for i in range(a,b):
    print(i)


for i in range(1,11,1):
    print("Hello", i)
print("*****************")
for i in range(10,101,10):
    print(i)
print("*****************")

for i in range(1,11,-1):
    print("Hello", i)

print("*****************")

for i in range(11,0,-1):
    print(i)
    if i == 5:
        break

