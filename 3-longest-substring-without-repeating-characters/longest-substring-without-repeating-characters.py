class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        result = 0
        l = 0
        for i in range(len(s)):
            map[s[i]] = 1 + map.get(s[i], 0)
            while map.get(s[i]) == 2:
                map[s[l]] = map.get(s[l]) - 1
                l += 1
            print(i, l, s[i], i - l + 1)
            result = max(result, i - l + 1)
        return result