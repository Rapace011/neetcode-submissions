class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            l, r= i+1, len(nums)-1

            if a == nums[i-1] and i > 0:
                continue

            while l < r:
                if a + nums[l] + nums[r] < 0:
                    l+=1
                elif a + nums[l]+ nums[r] > 0:
                    r-=1
                else:
                    res.append([a, nums[l], nums[r]])

                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res