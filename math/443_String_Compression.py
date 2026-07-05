# Input: chars = ["a","a","b","b","c","c","c"]
# ["a","2","b","2","c","3"]
# Output: 6
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].

chars = ["a","a","b","b","c","c","c"]


def compress(chars: list[str]) -> int:
    write, right = 0, 0
    count = 0
    while right < len(chars):
        current_char = chars[right]
        count = 0
        while right < len(chars) and current_char == chars[right]:
            count += 1
            right += 1

        chars[write] = current_char
        write += 1
        if count > 1:
            for chr in str(count):
                chars[write] = chr
                write += 1
    return write

print(compress(chars=chars))

