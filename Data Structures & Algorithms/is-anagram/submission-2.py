"""
Q: 
B:
- Dictionary (chars w/ counts); see if both dictionaries =
    - Time O(n+m)
    - Space O(n+m)
    Linear Time
T: 
Input: s = "racecar", t = "carrace"

s_counts = {r = 1; a = 1; c = 2; e = 1}
t_counts = {}

this is the reason i get meat from doordrash; i dont run though it
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        t_counts = {}
        for c in s:
            if c in s_counts.keys():
                s_counts[c] += 1
            else:
                s_counts[c] = 1
        for c in t:
            if c in t_counts.keys():
                t_counts[c] += 1
            else:
                t_counts[c] = 1
        return s_counts == t_counts

        