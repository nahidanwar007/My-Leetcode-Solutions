class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n

        for i in range(n):
            nums[i] = start + 2 * i
            if i > 0:
                nums[i] = nums[i-1] ^ nums[i]
        return nums[-1]
        