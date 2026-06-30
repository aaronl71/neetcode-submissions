class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        

        for ch in s:
            freqS[ch] = freqS.get(ch, 0) + 1

        freqT = {}

        for ch in t:
            freqT[ch] = freqT.get(ch,0) + 1
        
        return freqT == freqS
