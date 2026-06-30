class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #make hash table mapping val to index
        #iterate through list with two pointers,
        #making 'add' variable for every two number combo 
        #make 'neg' variable that is negative of 'add'
        #check if 'neg' is in hash table
        dict = {}
        dup_set = set()
        for i, v in enumerate(nums):
            dict[v] = i
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                add = nums[i] + nums[j]
                neg = -add
                if neg in dict and i != dict[neg] and j != dict[neg]:
                    t = tuple(sorted([nums[i], nums[j], neg]))
                    dup_set.add(t)
        output = list(dup_set)
        return output


