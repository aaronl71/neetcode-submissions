class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointers on opposite side of List
        #each step calculate amount of water using (j-i)*min(hieghts[i], heights[j])
        #move pointer that has smaller heigh value
        #use a max var to hold highest value
        l = 0
        r = len(heights) -1
        max = 0
        while l < r:
            
            temp = (r - l)*min(heights[l], heights[r])
            if temp > max:
                max = temp
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max


