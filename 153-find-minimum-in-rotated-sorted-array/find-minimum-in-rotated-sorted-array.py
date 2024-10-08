class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minimum = nums[0]
        

        while left <= right:
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])    
                break
            mid = (left + right) // 2

            minimum = min(minimum, nums[mid])
            print(minimum)
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minimum