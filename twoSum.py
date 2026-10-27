'''
Ex1: Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Ex2: Input: nums = [3,2,4], target = 6

Output: [1,2]

Ex3:

Input: nums = [3,3], target = 6

Output: [0,1]

'''
# Brutal solution
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# Time - O(n^2) Space - O(1)

def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res in dict:
            return [i, dict[res]] if i < dict[res] else [dict[res], i]
        dict[nums[i]] = i

print(twoSum([2,7,11,15], 9)) #[0, 1]
print(twoSum([3,2,4], 6)) #[1, 2]
print(twoSum([3,3], 6)) #[0, 1]

# Time - O(n)
# Space - O(n)
   

   