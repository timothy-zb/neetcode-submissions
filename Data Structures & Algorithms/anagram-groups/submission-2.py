class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = {}

        for str in strs :
            key = tuple(sorted(str))

            if key not in anagram :
                anagram[key] = []
            
            anagram[key].append(str)
        
        return list(anagram.values())
        
        