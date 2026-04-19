class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        out = []
        j = 0
        while j < len(s):
            i = j

            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])

            val = s[j+1: j+1+length]
            
            j = j + length + 1

            out.append(val)
        
        return out
            

            
        
