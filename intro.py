
message = 'Hello World!'

multi_line_message = """This is a multi-line message.
It spans several lines."""

print(message, multi_line_message)


# Find how many characters are in a string

#print(len(message))  # Output: 12
#print(len(multi_line_message))  # Output: 52


#print(message[5])
#print(message[0:5])  # Output: Hello. First index is inclusive, last index is exclusive.
#print(message[:5])   # Output: Hello. If starting index is omitted, it defaults to 0.
#print(message[6:])   # Output: World!. If ending index is omitted, it defaults to the length of the string.

# Convert to uppercase and lowercase
#print(message.lower()) # Output: hello world!
#print(message.upper()) # Output: HELLO WORLD!

# Count occurrences of a substring

#print(message.count('Hello'))
#print(message.count('o'))

#print(message.find('World'))  # Output: 6. Returns the starting index of the substring.
#print(message.find('Python')) # Output: -1. Returns -1 if the substring is not found.


# REPLACE

message.replace('World', 'Universe') # This does not change the original string since strings are immutable in Python.

new_message = message.replace('World', 'Universe')

print(new_message)

# Concatenating Strings

greeting = 'Hello'
name = 'Abdurrahman'

#full_greeting = greeting + ', ' + name

# Formatted String
#full_greeting = "{}, {}. Welcome!".format(greeting, name)

# f-String (Python 3.6+)
full_greeting = f"{greeting}, {name.capitalize()}. Welcome!"

print(full_greeting)  


# To see all string methods, you can use the dir() function
#print(dir(name))

# And to get help on a specific method, you can use the help() function
print(help(str.lower))