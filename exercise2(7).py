paragraph = input("Enter a paragraph: ")

text = paragraph.lower()

count = text.split().count("python")

print("The word 'python' appears", count, "times.")