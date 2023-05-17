string = input("Enter the string:") # Input taken fron user

list_word = string.split(' ') # converted each word in string in list item

d = {} # Created a empty Dictionary

for i in list_word:   # Iterate each list item through loop
    if i in d:        # Checks list item is present in dictionary or not
        d[i] = d[i] + 1
    else:
        d[i] = 1

max_freq_word = max(d, key=d.get) # returning maximum frequency word

print(max_freq_word,len(max_freq_word))  # Printing length of maximum freuquancy word