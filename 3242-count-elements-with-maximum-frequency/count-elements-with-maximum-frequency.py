class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        my_dict = {}
        for n in nums:
            my_dict[n] = 1 + my_dict.get(n, 0)
        my_dict_s = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

        print(my_dict_s)
        count = 0
        deg = 0
        for (key, val) in my_dict_s:
            if not deg:
                deg = val
                count += val
            elif val != deg:
                return count
            else:
                count += val
        return count

