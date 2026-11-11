class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        hasDuplicate = False

        for num in nums :
            if num in seen :
                hasDuplicate = True
                break
            else :
                seen.append(num)
        
        return hasDuplicate