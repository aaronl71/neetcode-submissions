class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1 
        output = []
        for r in range(len(nums)):
            if r - l + 1 == k:
                
                window = nums[l: r + 1]
                window.sort()
                output.append(window[-1])
                l += 1
        return output