class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()

        for num in nums:
            unique_set.add(num)

        if len(nums) == len(unique_set):
            return False
        else:
            return True