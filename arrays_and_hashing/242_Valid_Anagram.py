# Example 1:
#
s = "anagram"
t = "nagaram"
#
# Output: true
#
# Example 2:
# s = "aacc"
# t = "ccac"
#
# Output: false


def is_valid_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    d1 = {}
    d2 = {}
    for count_s1, count_s2 in zip(s1, s2):
        d1[count_s1] = d1.get(count_s1, 0) + 1
        d2[count_s2] = d2.get(count_s2, 0) + 1

    return d1 == d2


print(is_valid_anagram(s, t))

















# def is_valid_anagram(s1: str, s2: str) -> bool:
#     d = {}
#     if len(s1) != len(s2):
#         return False
#     for i in s1:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#
#     for i in s2:
#         if i not in d or d[i] <= 0:
#             return False
#         else:
#             d[i] -= 1
#     return True
#
# print(is_valid_anagram(s, t))