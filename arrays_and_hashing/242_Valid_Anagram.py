# Example 1:
#
# s = "anagram"
# t = "nagaram"
#
# Output: true
#
# Example 2:
s = "aacc"
t = "ccac"
#
# Output: false


def is_valid_anagram(s1: str, s2: str) -> bool:
    d = {}
    if len(s1) != len(s2):
        return False
    for i in s1:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for i in s2:
        if i not in d or d[i] <= 0:
            return False
        else:
            d[i] -= 1
    return True

print(is_valid_anagram(s, t))