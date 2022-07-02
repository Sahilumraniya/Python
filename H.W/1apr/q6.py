string = input("Enter String : ")
vowels = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
spaces = string.count(" ")
others = len(string) - vowels - spaces
print(f"Vowels: {vowels}\nSpaces: {spaces}\nOthers: {others}") 