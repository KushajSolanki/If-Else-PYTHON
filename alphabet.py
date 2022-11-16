ch = input("Enter a character:")
ch = ord(ch)
if(ch in range(65,91) or ch in range(97,123)):
    print("Alphabet")
else:
    print("Not alphabet")