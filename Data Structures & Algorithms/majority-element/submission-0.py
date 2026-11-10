class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        sorted_num = sorted(nums)

        return sorted_num[len(nums)//2]