def mixedcase(string):
    new = ""
    for i in range(0, len(string)):
        if i % 2 == 0:
            new += string[i].lower()
        else:
            new += string[i].upper()
    return new

text = input("Enter some text: ")

text = mixedcase(text)
print("Mixed case:", text)
