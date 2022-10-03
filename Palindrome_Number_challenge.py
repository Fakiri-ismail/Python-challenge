# Palindrome Number
def isPalindrome(x: int) -> bool:
    x = str(x)
    return x == x[::-1]

if __name__=='__main__':
    print(isPalindrome(-121))