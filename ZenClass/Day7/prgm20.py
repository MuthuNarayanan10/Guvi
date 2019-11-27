totalfreq = {} 
for i in test_str: 
    if i in all_freq: 
        totalfreq[i] += 1
    else: 
        totalfreq[i] = 1
  
 
print ("Count of all characters in GuviGeeksZenClass :\n "
                                        +  str(totalfreq)) 
