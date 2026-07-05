# input: s = "AAAAABBBCDDDDEEFEF"
# output: A5B3C1D4E2F1E11


def compress(s: str) -> list[str]:
    count = 1
    res = []
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            count += 1
        else:
            res.append(s[i-1])
            res.append(str(count))
            count = 1
        print(res)
    res.append(s[-1])
    res.append(str(count))

    return "".join(res)

print(compress("AAAAABBBCDDDDEEFEF"))