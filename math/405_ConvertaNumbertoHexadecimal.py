# Example 1:
#
# Input: num = 26
# Output: "1a"
# Example 2:
#
# Input: num = -1
# Output: "ffffffff"

d = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}


def convert_to_hex(num: int) -> str:
    num &= 0xFFFFFFFF

    if num == 0:
        return "0"

    def helper(n: int) -> str:
        if n < 16:
            return d[n] if n in d else str(n)

        res = n % 16
        cur_char = d[res] if res in d else str(res)
        cur_del = n // 16

        return helper(cur_del) + cur_char

    return helper(num)

num = 422
print(convert_to_hex(num))