# Longest Common Prefix
def longestCommonPrefix(strs) -> str:
    if len(strs) == 1:
        return strs[0]

    strs = sorted(strs, key=lambda x: len(x))
    short_word = strs[0]
    common_prefix = ''
    for i in range(1, len(short_word)+1):
        for word in strs[1:]:
            if not word.startswith(short_word[:i]):
                return common_prefix
        common_prefix = short_word[:i]
    return common_prefix

# Palindrome Number
def isPalindrome(x: int) -> bool:
    x = str(x)
    return x == x[::-1]

# Valid Parentheses
def isValid(s: str) -> bool:
    if s.startswith((')', '}', ']')) or s.count('(') != s.count(')') or \
        s.count('[') != s.count(']') or s.count('{') != s.count('}'):
        return False
    char = {')': '(', '}': '{', ']': '['}
    good = []
    for i in s:
        if i in char.values():
            good.append(i)
        else:
            try:
                if char[i] == good[-1]:
                    del good[-1]
                else:
                    return False
            except:
                return False
    return len(good) == 0



if __name__=='__main__':
    print(isValid("(){}}{"))
