class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mydict = {}

        for n in nums:
            mydict[n] = 1 + mydict.get(n, 0)
        
        mydict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
        freq = defaultdict(list)

        for key, val in mydict.items():
            freq[val].append(key)
        print(freq)
        first_key, first_val = list(freq.items())[0]
        print(first_val)

        return len(first_val)*first_key


