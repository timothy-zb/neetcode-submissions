class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_s = {}
        string_t = {}

        for ch in s :
            if ch not in string_s :
                string_s[ch] = 1
            else :
                string_s[ch]+=1
        
        for ch in t :
            if ch not in string_t :
                string_t[ch] = 1
            else :
                string_t[ch]+=1
        
        return string_t == string_s

        