# Define the function the_last_word, which takes a string as input.
def the_last_word(a_string):
    # Define a format string for printing input and sorting method.
    fmt = "For Input: {:18}    Sort Using: {}"
    
    # Extract the last word (presumably last name) from the input string.
    last_word = a_string.strip().split()[-1]
    
    # Print the original input and the last word used for sorting.
    print(fmt.format(a_string, last_word))
    
    # Return the last word.
    return last_word

# Define a string containing a list of names separated by commas and spaces.
names = """Ava Smith, Ethan Johnson, Abigail Williams, \
Sophia Brown, Michael Jones, Emily Miller, Declan Lee"""

# Split the string into a list of names using the delimiter ", ".
names = names.split(", ")

# Sort the list of names using the the_last_word function as the sorting key.
names.sort(key=the_last_word)

# Print the sorted list of names.
print(names)