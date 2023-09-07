# Prompting user for greeting
greeting = input("Greeting: ")

# Splitting string into individual words
greeting_words = greeting.lower().split()

# Applying different conditions on the string
if greeting_words[0] == "hello" or greeting_words[0] == "hello,":
    print("$0")
elif greeting_words[0][0] == "h":
    print("$20")
else:
    print("$100")

