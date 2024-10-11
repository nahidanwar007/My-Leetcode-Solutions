class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        max_freq = max(freq_map.values())
        
        result = 0
        for num, freq in freq_map.items():
            if freq == max_freq:
                result += freq
                
        return result


