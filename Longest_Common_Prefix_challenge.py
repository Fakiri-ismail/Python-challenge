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


if __name__=='__main__':
    print(longestCommonPrefix(["ab", "a"]))
