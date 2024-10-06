class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map_f = {}
        map_s = {}
        for i in range(26):
            map_f[chr(i+97)] = 0
            map_s[chr(i+97)] = 0
            
        for i in range(len(s1)):
            map_f[s1[i]] += 1
            map_s[s2[i]] += 1
        
        if map_s == map_f:
                return True
        l = 0

        for j in range(len(s1), len(s2)):
            map_s[s2[j]] += 1
            map_s[s2[l]] -= 1
            l += 1
            if map_s == map_f:
                return True
                
        return False