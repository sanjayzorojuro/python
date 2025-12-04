def pali(s):
    if s == s[::-1]:
        return True
    return False

s=input("Enter a string to check for palindrome:")
print(pali(s))