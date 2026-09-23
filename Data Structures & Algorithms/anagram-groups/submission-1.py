from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def computeFrequency(string: str):
            frequency = [0] * 26 # Number of english letters
            offset = ord('a')
            for character in string:
                index = ord(character) - offset
                frequency[index] += 1
            return tuple(frequency)
        
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
