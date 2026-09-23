from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for string in strs:
            sortedS = ''.join(sorted(string))
            results[sortedS].append(string)
        return list(results.values())
