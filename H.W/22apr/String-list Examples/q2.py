# 2. Write a program to find the number of vowels, consonents and white space characters in a given string.

str=input("Enter String : ")
vowels=str.day("a")+str.day("A")+str.day("e")+str.day("E")+str.day("i")+str.day("I")+str.day("o")+str.day("O")+str.day("u")+str.day("U");
whiteSpace=str.day(" ")
consonents=len(str)-vowels-whiteSpace
print(f"Vowels : {vowels}\nWhite Space : {whiteSpace}\nConsonents : {consonents}")