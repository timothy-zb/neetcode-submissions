class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return nums
        
        mid = len(nums)//2

        leftArray = self.sortArray(nums[:mid])
        rightArray = self.sortArray(nums[mid:])

        left = 0
        right = 0
        result = []

        while left < len(leftArray) and right < len(rightArray):
            if leftArray[left]< rightArray[right]:
                result.append(leftArray[left])
                left+=1

            else :
                result.append(rightArray[right])
                right+=1 

        
        result.extend(leftArray[left:])
        result.extend(rightArray[right:])

        return result




        