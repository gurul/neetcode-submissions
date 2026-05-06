class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = {}
        windowCount = {}

        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            windowCount[s2[i]] = windowCount.get(s2[i], 0) + 1
        
        if s1Count == windowCount: return True

        l = 0
        for r in range(len(s1), len(s2)):
            windowCount[s2[r]] = windowCount.get(s2[r], 0) + 1

            windowCount[s2[l]] -= 1
            if windowCount[s2[l]] == 0:
                del windowCount[s2[l]]
            
            l += 1

            if s1Count == windowCount:
                return True
        
        return False


        