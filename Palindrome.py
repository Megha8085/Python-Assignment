word=str(input("Enter any word to check is palindrome or not "));
if word == word[::-1]:
    print("Given Word is Palindrome")
else:
    print("Given Word is not Palindrome")
