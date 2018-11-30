#Check if the string is palindrome.

string=input("Enter the string: ")
new_string = string[-1::-1]

if string == new_string:
    print("The String is palindrome")
else:
    print("The String is not palindrome")