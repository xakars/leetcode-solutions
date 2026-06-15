# Example 1:
#
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
#
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
#
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


def fuzz_buzz(n: int):
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res

print(fuzz_buzz(15))



# def fuzz_buzz(n: int):
#     res = []
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             res.append("FizzBuzz")
#         elif i % 3 == 0 or i % 5 == 0:
#             if i % 3 == 0:
#                 res.append("Fizz")
#             else:
#                 res.append("Buzz")
#         else:
#             res.append(str(i))
#
#     return res
#


