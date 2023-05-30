def is_valid_string(s):

    freq_table = {}  # Create a frequency table
    for char in s:

        freq_table[char] = freq_table.get(char, 0) + 1 # All repeated charcter incremented by 1 and stored in the dictionary as values.
                                                       

    frequencies = list(freq_table.values())  # Count the frequency of each character
    print(frequencies)
    max_freq = max(frequencies) # Finding the most frequent characters
    min_freq = min(frequencies) # Finding the least frequent characters
    
    if max_freq == min_freq: # Checking All characters have the same frequency
        return "YES"
    elif (frequencies.count(min_freq)) > (frequencies.count(max_freq)): # Checking the string after removal of one extra character 
        return "YES"
    else:
        return "NO"
    
user_input = input('Enter any string: ')
print(is_valid_string(user_input))

