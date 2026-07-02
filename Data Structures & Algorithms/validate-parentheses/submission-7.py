class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        opening_brak = ["{", "(", "["]
        closing_brak = ["}", ")", "]"]
        brakets = {")": "(", "]": "[", "}": "{"}
   

        for i in range(len(s)):
            if s[i] in opening_brak:
                stk.append(s[i])
            else:
                if len(stk) == 0:
                    return False

                if stk[-1] != brakets[s[i]]:
                    return False
                stk.pop()   
            
        return len(stk) == 0
