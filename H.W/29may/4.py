# Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.

d={'Right':'Left','up':'down'}
print(d)
s=input("\nEnter string : ")
print(d[s.lower()])