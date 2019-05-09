# checks if a give string is a palindrome
def reverse_string(s):
    return s[::-1]
given_string = input("Enter a string: ")
rev_string = reverse_string(given_string)
if given_string == rev_string:
    print("This string is a palindrome.")
else:
    print("This string is not a palindrome.")