# Input:
s = "()[]{}"
#
# Output: true
# Input: s = "([])"
#
# Output: true
# Input: s = "([)]"
#
# Output: false
def valid_parentheses(s: str) -> bool:
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = []
    for i in s:
        if i in pairs:
            stack.append(i)
        else:
            if not (stack and pairs[stack.pop()] == i):
                return False

    return not stack

print(valid_parentheses(s))