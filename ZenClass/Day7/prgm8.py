string = input("Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("\nAlphabets in this String :  ", alphabets)
print("Digits in this String :  ", digits)
print("Special Characters in this String :  ", special)