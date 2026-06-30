class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #iterate through str making substrs with sliding window
        #var counting diff between len of substr and most freq char
        #the solution contains the longest substr that has at most k replacements
        from collections import Counter
        l = 0
        best = 0
        for r in range(len(s)):
            substr = s[l:r + 1]
            substr_freq = Counter(substr)
            num_most_freq_char = substr_freq.most_common(1)[0][1]
            diff = len(substr) - num_most_freq_char
            while diff > k:
                l+=1

                substr = s[l:r + 1]
                substr_freq = Counter(substr)
                num_most_freq_char = substr_freq.most_common(1)[0][1]
                diff = len(substr) - num_most_freq_char
            best = max(best, len(substr)) 
        return best


            



