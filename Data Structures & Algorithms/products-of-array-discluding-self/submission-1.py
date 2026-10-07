class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        sufix = [1]
        for i in range(len(nums) - 1):
            prefix.append(prefix[i] * nums[i])
            sufix.append(sufix[i] * nums[len(nums) - 1 - i])
        
        res = [prefix[i] * sufix[len(nums) - 1 - i] for i in range(len(nums))]
        return res