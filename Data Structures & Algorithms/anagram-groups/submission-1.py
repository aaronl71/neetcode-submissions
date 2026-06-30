class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashAnagram = {} # chars : string
        for str in strs:
            sorted_str = " ".join(sorted(str))
            hashAnagram.setdefault(sorted_str, []).append(str)
        return list(hashAnagram.values())
        