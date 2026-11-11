class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_map = {}
        result = set()

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

            if count_map[num] > len(nums) // 3:
                result.add(num)

        return list(result)