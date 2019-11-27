string = input("enter your own String : ")
char = input("enter your own Character : ")

flag = 0
for i in range(len(string)):
    if(string[i] == char):
        flag = 1
        break

if(flag == 0):
    print("no charater ")
else:
    print( " is Found at Position " , i + 1)