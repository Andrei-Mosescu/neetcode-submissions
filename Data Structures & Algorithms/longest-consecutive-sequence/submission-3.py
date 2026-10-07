class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        max = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i] - 1:
                cur += 1
            elif nums[i-1] != nums[i]:
                cur = 1
            if cur > max:
                max = cur
        
        return max
        