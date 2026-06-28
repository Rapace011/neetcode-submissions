class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = {}
        frequency_t = {}

        if len(s) != len(t):
            return False

        for i in s:
            frequency_s[i] = frequency_s.get(i, 0)+1
        
        for i in t:
            frequency_t[i] = frequency_t.get(i, 0)+1

        if frequency_s == frequency_t:
            return True
        return False