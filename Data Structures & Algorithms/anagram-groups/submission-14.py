class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map each word to letter count
        # using array of 26 chars for wordmap
        # ord -> integer using unicode of char
        anagrams = {}
        for string in strs:
            wordmap = [0] * 26
            for char in string:
                wordmap[ord(char) - ord("a")] += 1
            strin = ''.join(str(wordmap))
            if strin in anagrams:
                anagrams[strin].append(string)
            else:
                anagrams[strin] = [string]
        final = []
        for key, value in anagrams.items():
            final.append(value)
        return final