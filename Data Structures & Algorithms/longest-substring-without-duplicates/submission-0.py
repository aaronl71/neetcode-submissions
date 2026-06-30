class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dynamic sliding window
        # iterate through str with dynamic sliding window
            # after each iteration moving r, check if char is not current set
            # if repeat char is found move l
        #make hashset
        duplicate = set()
        cur = 0
        best = 0
        l = 0
        for r in range(len(s)):
            while s[r] in duplicate:
                duplicate.remove(s[l])
                l+=1

            duplicate.add(s[r])
            cur = r - l + 1
            best = max(cur, best)
            
        return best

            




            
