class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mmap = {}
        for n in nums:
            mmap[n] = 1 + mmap.get(n, 0)
        
        mmap = dict(sorted(mmap.items(), key=lambda item: item[1], reverse=True))
        
        ans = list(mmap.keys())
        
        return ans[:k]