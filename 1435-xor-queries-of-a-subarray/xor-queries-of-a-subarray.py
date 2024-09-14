from functools import reduce 
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefixXOR = [0] * n
        prefixXOR[0] = arr[0]
        
        # Fill the prefixXOR array
        for i in range(1, n):
            prefixXOR[i] = prefixXOR[i - 1] ^ arr[i]
        
        # Step 2: Compute results for each query
        result = []
        for left, right in queries:
            if left == 0:
                result.append(prefixXOR[right])
            else:
                result.append(prefixXOR[right] ^ prefixXOR[left - 1])
        
        return result
