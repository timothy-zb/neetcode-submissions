class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        substring = strs[0]

        for word in strs[1:]:
            while substring != word[:len(substring)]:
                substring = substring[:-1]

        return substring