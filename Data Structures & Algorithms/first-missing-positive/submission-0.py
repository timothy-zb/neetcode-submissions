class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i =1
        while i > 0:
            if i not in nums :
                return i
            i+=1
        
        return 0
        
        