class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 strings, s & t
        # first case: not the same length = instant fail
        if len(s) != len(t):
            return False
        occ = dict()
        occ_2 = dict()
        for letter in s:
            if letter not in occ:
                occ[letter] = 1
            else:
                occ[letter] += 1
        for letter in t:
            if letter not in occ_2:
                occ_2[letter] = 1
            else:
                occ_2[letter] += 1
        if occ == occ_2:
            return True
        return False