def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])


word = input("Enter a word: ")
if is_palindrome(word) == True:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
