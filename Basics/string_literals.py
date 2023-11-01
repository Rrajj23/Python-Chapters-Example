print("This is a literal string", 'and so is this')
print('"Double quotes" inside of single quotes')
print("'Single quotes' inside of double quotes")
print("A double quote  inside double quotes")
print(r"A double quote  inside a raw literal string")
print("A as unicode: \x41")
# so here the \x41 is escape sequence representing the unicode character with hexadecimal code point 41 . 
# so here the 41 is hec=xdecimal value that correspond the decimal value as 65

spades = """Royal Straight Flush\
\U0001F0A1 \U0001F0AE \U0001F0AD \U0001F0AB \U0001F0AA
"""
# the spade here represent a multi line string in python containing representation of "royal staright flush" in a card game 
# the spade suit is typlically represent by a black leaf in card game 
# U0001F0A1 there are the unicode point represent while playing cards for the spades suits 
# where each \U escape sequence is followed by eight digit hexadecimal number representing the unicode point for a specific playing card
 
print(spades)

diamonds = """Royal Straight Flush
\U0001F0C1 \U0001F0CE \U0001F0CD \U0001F0CB \U0001F0CA
"""
print(diamonds)
print("Emoticons 😎 😮 😰 😱 😴")