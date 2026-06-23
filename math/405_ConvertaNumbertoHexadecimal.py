# Example 1:
#
# Input: num = 26
# Output: "1a"
# Example 2:
#
# Input: num = -1
# Output: "ffffffff"

d = {
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f"
}
res_fin = []

def convert_to_hex(num: int):
    if num // 16 == 0:
        res_fin.append(1)
        return 1
    cur_del = num // 16
    tmp = cur_del * 16
    res = num - tmp
    if res in d:
        res_fin.append(d[res])
    else:
        res_fin.append(res)
    return convert_to_hex(cur_del)

print(res_fin)
print(convert_to_hex(422))
print(res_fin)