# Input:
# s = "IceCreAm"
# Output: "AceCreIm"
# Input: s = "leetcode"
# Output: "leotcede"


s = "IceCreAm"
def reverse_vowels(s: str) -> str:
    v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    l, r = 0, len(s) - 1
    s = list(s)
    while l < r:
        if s[l] not in v:
            l += 1
            continue
        if s[r] not in v:
            r -= 1
            continue
        if s[l] in v and s[r] in v:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    return "".join(s)



    return None

print(reverse_vowels(s))



