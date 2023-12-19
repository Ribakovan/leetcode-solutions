class Solution:
    def groupAnagram(self, strs: list[str]) -> list[list[str]]:
        result = {}
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord("a")] += 1
            key = tuple(counts)
            if key not in result:
                result[key] = []
            result[key].append(word)
        return result.values()