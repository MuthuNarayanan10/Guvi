
str1 = input("enter your own String : ")
ch = input("enter your own Character : ")

for i in range(len(str1)):
    if(str1[i] == ch ):
        print(ch, " is Found at Position " , i + 1)