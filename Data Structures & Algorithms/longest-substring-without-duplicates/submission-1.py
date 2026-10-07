class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        let = {}
        maxi = 0
        for r in range(len(s)):
            if s[r] in let:
                l = max(l, let[s[r]]+1)
            let[s[r]] = r
            maxi = max(maxi, r-l+1)
        return maxi
        