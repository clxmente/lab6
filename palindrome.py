def is_palindrome(s: str) -> bool:
    s2 = ''.join(char for char in s if s.isalnum())
    return s.lower() == s2.lower()[::-1]

if __name__ == '__main__':
    string = input("Enter a string: ")
    if is_palindrome(string):
        print("Palindrome")
    else:
        print("Not a palindrome")
