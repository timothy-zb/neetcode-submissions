class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            complement = target - num

            if complement in nums[i+1:]:
                j = nums.index(complement, i+1)
                return [i, j]