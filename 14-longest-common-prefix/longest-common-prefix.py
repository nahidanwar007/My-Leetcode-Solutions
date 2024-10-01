class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # strs.sort()
        # first = strs[0]
        # last = strs[-1]

        # res = ""

        # for i in range(min(len(first), len(last))):
        #     if first[i] != last[i]:
        #         return res
        #     res += first[i]
        # return res

        # Solution - 2
        res = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or strs[0][i] != word[i]:
                    return res
            res += strs[0][i]
        return res