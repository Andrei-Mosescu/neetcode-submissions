class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqDict = defaultdict(list)
        for s in strs:
            freq = [0] * 32
            for c in s:
                freq[ord(c) - ord('a')] = freq[ord(c) - ord('a')] + 1
            freqK = tuple(freq)
            freqDict[freqK].append(s)
        return list(freqDict.values())
        