class Solution:
    def encode(self, strs: List[str]) -> str:
        #len of word before word
        sol = ""
        for string in strs:
            sol += str(len(string)) + '#' + string
        return sol

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            next_hash = s.find('#')
            count = int(s[0:next_hash])
            s = s[next_hash + 1:]
            strs.append(s[:count])
            s = s[count:]
        return strs

