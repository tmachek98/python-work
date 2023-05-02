#Code to let the user input a message then we give verious feedback.

message = input("Enter a message: ")

#Using functions to return back the message with a new variation to it.

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

#Using the split function each word will be separated to their own sub-string.

words = message.split()
print("Words:", words)

#Creating a new variable to sort the words alphabetically.

sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])

