# Problem: https://leetcode.com/problems/two-sum/
# Time: O(n), Space: O(n)

def twoSum(nums, target):
    num_map = {}  # value: index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]
 
