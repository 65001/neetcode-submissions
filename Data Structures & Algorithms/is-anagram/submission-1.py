from collections import defaultdict

class Solution:
    

    def isAnagram(self, s: str, t: str) -> bool:
        def generateFrequencyDictionary(string: str) -> dict:
            dictionary = defaultdict(int)
            for character in string:
                dictionary[character] += 1
            return dictionary
        return generateFrequencyDictionary(s) == generateFrequencyDictionary(t)