class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            anagramDict[sortedS].append(s)
        return list(anagramDict.values())
