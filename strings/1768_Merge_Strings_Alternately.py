word1 = "abc"
word2 = "pqr"


#$O(N + M) - где N и M — длины строк s1 и s2
def merge_str(s1: str, s2: str) -> str:
    l1, l2 = 0, 0
    res = []
    while l1 < len(s1) or l2 < len(s2):
        if l1 < len(s1):
            res.append(s1[l1])
            l1 += 1
        if l2 < len(s2):
            res.append(s2[l2])
            l2 += 1

    return "".join(res)

print(merge_str(word1, word2))



# def merge_str(s1: str, s2: str) -> str:
#     longest_word = max(len(s1), len(s2))
#     l1 = 0
#     l2 = 0
#     res = ""
#     while longest_word >= 0:
#         if l1 < len(s1):
#             res += s1[l1]
#             l1 += 1
#         if l2 < len(s2):
#             res += s2[l2]
#             l2 += 1
#
#         longest_word -= 1
#
#     return res
#
# # word1 = "abc"
# # word2 = "pqr"
#
# print(merge_str(word1, word2))