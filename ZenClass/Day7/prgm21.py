string = input("enter your own String : ")
char = input("enter your own Character : ")
string2 = ''
length = len(string)
for i in range(length):
    if(string[i] == char):
        string2 = string[0:i] + string[i + 1:length]
        break
 
print("Final String :     ", string2)