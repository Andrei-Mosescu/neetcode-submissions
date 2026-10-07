class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        window = {}
        l = 0
        have = 0
        need = len(countT)
        res, reslen = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and countT[c] == window[c]:
                have += 1
            while need == have:
                window[s[l]] = window[s[l]] - 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    if r-l+1 < reslen:
                        reslen = r-l+1
                        res = [l, r]
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""

