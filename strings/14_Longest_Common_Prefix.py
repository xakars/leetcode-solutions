# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

strs = ["aa","a"]


def longest_prefix(strs: list) -> str:
    res = []
    prefix = strs[0]
    for i in range(len(prefix)):
        for j in strs[1:]:
            if i >= len(j) or j[i] != prefix[i]:
                return "".join(res)
        res.append(prefix[i])
    return "".join(res)

print(longest_prefix(strs))