class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1+ count.get(n, 0)
        
        freq_list = [[] for i in range(len(nums) + 1)]
        for key, v in count.items():
            freq_list[v].append(key)
        
        res = []
        for i in range(len(freq_list) - 1, 0, -1):
            for v in freq_list[i]:
                res.append(v)
                if k == len(res): 
                    return res