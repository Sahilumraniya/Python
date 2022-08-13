string = input("Enter String : ")
vowels = string.day("a") + string.day("e") + string.day("i") + string.day("o") + string.day("u")
spaces = string.day(" ")
others = len(string) - vowels - spaces
print(f"Vowels: {vowels}\nSpaces: {spaces}\nOthers: {others}") 