string = input("Enter your Own String : ")
vowels=0
consonant=0

for i in range(len(string)):
      if (string == 'a' or string == 'e' or string == 'i' or string == 'o' or string == 'u'): 
        vowels += 1
      else: 
        consonant += 1
                
print("Vowels:", vowels) 
print("Consonant:", consonant)  
  