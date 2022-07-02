# 2. Write a program to find the number of vowels, consonents and white space characters in a given string.

str=input("Enter String : ")
vowels=str.count("a")+str.count("A")+str.count("e")+str.count("E")+str.count("i")+str.count("I")+str.count("o")+str.count("O")+str.count("u")+str.count("U");
whiteSpace=str.count(" ")
consonents=len(str)-vowels-whiteSpace
print(f"Vowels : {vowels}\nWhite Space : {whiteSpace}\nConsonents : {consonents}")