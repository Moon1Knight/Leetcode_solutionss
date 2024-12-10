from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        # If nums has fewer than 2 elements, there can be no adjacent pairs
        if n < 2:
            return [True] * len(queries)
        
        same_parity = [nums[i] % 2 == nums[i + 1] % 2 for i in range(n - 1)]
        prefix_sum = [0] * (n - 1)
        prefix_sum[0] = int(same_parity[0])
        
        for i in range(1, n - 1):
            prefix_sum[i] = prefix_sum[i - 1] + int(same_parity[i])
        
        result = []
        for fromi, toi in queries:
            if toi == fromi:  # Subarray with only one element is always special
                result.append(True)
            else:
                count_same_parity = prefix_sum[toi - 1] - (prefix_sum[fromi - 1] if fromi > 0 else 0)
                result.append(count_same_parity == 0)
        
        return result
