from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def computeFrequency(string: str) -> set:
            dictionary = defaultdict(int)
            for character in string:
                dictionary[character] += 1
            return frozenset( dictionary.items() )
        
        frequencyToGroupIndex = {}
        groups = []
        groupCounter = 0

        for string in strs:
            fs = computeFrequency(string)
            groupIndex = frequencyToGroupIndex.get(fs)
            if groupIndex is None:
                # We have found a new group!
                frequencyToGroupIndex[fs] = groupCounter
                groupCounter += 1
                groups.append([string])
            else:
                # We need to add onto an existing group
                groups[groupIndex].append(string)
        return groups
