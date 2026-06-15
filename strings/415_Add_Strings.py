# Example 1:
#
# Input: num1 = "11", num2 = "123"
# Output: "134"



num1 = "9"
num2 = "1"


def add_string(s1: str, s2: str) -> str:
    rem = 0
    res = []
    r1 = len(s1) - 1
    r2 = len(s2) - 1
    while r1 >= 0 or r2 >=0:
        digit1 = ord(s1[r1]) - ord('0') if r1 >= 0 else 0
        digit2 = ord(s2[r2]) - ord('0') if r2 >= 0 else 0
        cur = digit1 + digit2 + rem

        res.append(str(cur % 10))
        rem = cur // 10

        r1 -= 1
        r2 -= 1
    if rem:
        res.append(str(rem))
    return "".join(res)[::-1]

print(add_string(num1, num2))