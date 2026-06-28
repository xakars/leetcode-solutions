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
    if num < 16:
        return d[num] if num in d else str(num)
    res = num % 16
    cur_char = d[res] if res in d else str(res)
    cur_del = num // 16
    return convert_to_hex(cur_del) + cur_char

num = 422
print(convert_to_hex(num))