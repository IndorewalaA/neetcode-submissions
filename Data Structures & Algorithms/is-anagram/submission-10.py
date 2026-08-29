class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 strings, s & t
        s_list = list(s)
        s_list.sort()
        t_list = list(t)
        t_list.sort()
        if s_list == t_list:
            return True
        return False