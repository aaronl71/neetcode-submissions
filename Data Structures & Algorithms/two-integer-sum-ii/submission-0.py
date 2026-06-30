class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #make a dict mapping index to val
        dict = {}
        #iterate through list, for each iteration find value that is target - list[i]
        #check if that value is in hashtable
        #if value is in hashtable add index to list check which index is lower then add lower 
        #index first 
        output = []

        for i, v in enumerate(numbers):
            diff = target - numbers[i]
            if diff not in dict:
                dict[v] = i
            elif diff in dict:
                if i < dict[diff]:
                    output.append(i + 1)
                    output.append(dict[diff] + 1)
                else:
                    output.append(dict[diff] + 1)
                    output.append(i + 1)
        return output
        
                
        
        
