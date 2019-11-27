mystr = "Remove last occurrence of a BAD word. This is a last BAD word."

removal = "BAD"
reverse_removal = removal[::-1]

replacement = "GOOD"
reverse_replacement = replacement[::-1]

newstr = mystr[::-1].replace(reverse_removal, reverse_replacement, 1)[::-1]
print ("mystr:", mystr)
print ("newstr:", newstr)