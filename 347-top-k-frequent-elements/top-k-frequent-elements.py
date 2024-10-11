class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # mmap = {}
        # for n in nums:
        #     mmap[n] = 1 + mmap.get(n, 0)
        
        # mmap = sorted(mmap.items(), key=lambda item: item[1], reverse=True)
        
        # return [item[0] for item in mmap[:k]]

        # bucket sort solution

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        freq = [[] for i in range(len(nums)+1)]

        for key, val in count.items():
            freq[val].append(key)
        
        res = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res