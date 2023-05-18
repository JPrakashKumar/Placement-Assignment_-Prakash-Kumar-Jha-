def is_valid_string(s):

    freq_table = {}  # Create a frequency table
    for char in s:

        freq_table[char] = freq_table.get(char, 0) + 1 # All repeated charcter incremented by 1 and stored in the dictionary as values.
                                                       

    frequencies = list(freq_table.values())  # Count the frequency of each character

    max_freq = max(frequencies) # Finding the most frequent characters
    min_freq = min(frequencies) # Finding the least frequent characters

    if max_freq == min_freq: # Checking All characters have the same frequency
        return "YES"
    
    elif max_freq - min_freq == 1 and min_freq == 1: # Checking the case after removing one character form the input string
        return "YES"

    else:
        return "NO"
    
user_input = input('Enter any string: ')
print(is_valid_string(user_input))

