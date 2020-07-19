'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dict = {}
        for each in range(len(nums)):
            if target - nums[each] in number_dict.keys():
                return sorted([each, number_dict[target - nums[each]]])
            number_dict[nums[each]] = each