number = int(input("Number:"))
for x in range(0,number):
    for y in range(0,number-x-1):
        print(end=" ")
    for y in range(0,x+1):
        print("*",end=" ")
    print()
