s=input("Enter the text:")
text = str(s)
if len(set(text)) >= 26:
    print("True")
else:
    print("False")
