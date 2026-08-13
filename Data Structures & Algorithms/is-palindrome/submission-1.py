class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = [x.lower() for x in s if x.isalnum()]
        l, r = 0, len(s1)-1

        while l <= r:
            if s1[l] != s1[r]:
                return False
            else:
                l +=1
                r -= 1
        
        return True