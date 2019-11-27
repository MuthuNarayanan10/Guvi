string = input("enter your own String : ")
char = input("enter your own Character : ")

flag = -1
for i in range(len(string)):
    if(string[i] == char):
        flag = i
        break

if(flag == -1):
    print("no charater ")
else:
    print( " is Found at Position " , flag+ 1)