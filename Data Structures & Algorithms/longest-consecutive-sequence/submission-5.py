class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        maxl = 0
        leng = 0
        for n in nums:
            if n-1 not in nset:
                leng = 1
                while n+leng in nset:
                    leng += 1
                
            maxl = max(maxl, leng)
        return maxl