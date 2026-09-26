class Solution:
    def encode(self, strs: List[str]) -> str:
        # Add '#' after the length so we know where the length ends
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            # Find the index of the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract the length (everything between i and j)
            length = int(s[i:j])
            
            # Move index past '#' to the start of the string
            i = j + 1
            
            # Extract the string using the length
            strs.append(s[i : i + length])
            
            # Move index past the current string
            i += length
            
        return strs