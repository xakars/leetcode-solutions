nums = [3,2,4]
target = 6


# x + y = target
# x = target - y
def find_sum_two(nums: list, target: int) -> list[int]:
    seen = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [seen[need], i]
        seen[nums[i]] = i
    return []


#0(n^2)
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if target == nums[i] + nums[j]:
#             print(i, j)