text = input("Enter a string: ")

print(len(text))

text = text.upper()

text = text.replace(" ", "_")

text = text.split("_")

print(text)