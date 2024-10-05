class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        map = {}
        l = 0
        res = 0
        for i in range(len(s)):

            map[s[i]] = 1 + map.get(s[i], 0)
            while 3 in map.values():
                map[s[l]] = map.get(s[l]) - 1
                l += 1
            print(s[l:i+1])
            res = max(res, i - l + 1)
        return res
