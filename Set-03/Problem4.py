def is_palindrome(word):
    word = word.lower()
    
    if word == word[::-1]:
        return True
    else:
        return False

word = input("Enter word:")
if is_palindrome(word):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")
