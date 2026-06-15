# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    inp = x
    res = 0
    while inp > 0:
        res = res * 10 + inp % 10
        inp = inp // 10

    return x == res

print(is_palindrome(121))