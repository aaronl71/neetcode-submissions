class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        freqt = Counter(t)
        l = 0
        result = ""
        
        for r in range(len(s)): #iterate through s with right pointer
            freq_sub = Counter(s[l: r + 1])
            while freqt <= freq_sub:
                freq_sub[s[l]] -= 1
                substr = s[l: r + 1]
                if result == "" or len(substr) < len(result):
                    result = substr
                l += 1 
                
        return result
            
        
            

            
            
