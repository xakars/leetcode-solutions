# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
#[-4, -1, -1, 0, 1, 2]


nums = [-1, 0, 1, 2, -1, -4]

def three_sum(nums: list[int]) -> list[int]:
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, len(nums)-1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and  nums[l] == nums[l+1]:
                    l += 1
                while l < r and  nums[r] == nums[r-1]:
                    r -= 1
            elif curr_sum > 0:
                r -= 1
            else:
                l += 1

    return res


print(three_sum(nums))