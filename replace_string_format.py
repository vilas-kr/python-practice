templete_string = "Hello <<UserName>>, How are you?"
name = input("Enter your name: ")
while(len(name) < 3):
    print("Please enter a name with at least 3 characters.")
    name = input("Enter your name: ")
final_string = templete_string.replace("<<UserName>>", name)
print(final_string)
