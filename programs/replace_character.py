# Write a Java program that takes a string as input, replaces all 
# occurrences of a specified character with another specified character, 
# and then returns the modified string.

s = input("Enter a string : ")
old_char = input("Enter character to be replaced : ")
new_char = input("Enter replace character : ")

s = s.replace(old_char, new_char)
print(f"New string is : {s}")