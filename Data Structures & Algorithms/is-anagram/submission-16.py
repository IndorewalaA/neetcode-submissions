class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 strings, s & t
        # first case: not the same length = instant fail
        if len(s) != len(t):
            return False
        occ, occ_2 = {}, {}
        for i in range(len(s)):
            occ[s[i]] = 1 + occ.get(s[i], 0)
            occ_2[t[i]] = 1 + occ_2.get(t[i], 0)
        if occ == occ_2:
            return True
        return False