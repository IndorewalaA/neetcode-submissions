class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given strs, group all anagrams together into sublists
        # return in any order
        anagrams = dict()
        for string in strs:
            alpha = ''.join(sorted(string))
            if alpha in anagrams:
                anagrams[alpha].append(string)
            else:
                anagrams[alpha] = [string]
        final = []
        for entry, key in anagrams.items():
            final.append(key)
        return final