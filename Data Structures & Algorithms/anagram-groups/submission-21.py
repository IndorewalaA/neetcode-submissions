class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map each word to letter count
        # using array of 26 chars for wordmap
        # ord -> integer using unicode of char
        anagrams = defaultdict(list)
        for string in strs:
            wordmap = [0] * 26
            for char in string:
                wordmap[ord(char) - ord("a")] += 1
            anagrams[tuple(wordmap)].append(string)
        return list(anagrams.values())