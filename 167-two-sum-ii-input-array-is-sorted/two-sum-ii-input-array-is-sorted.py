class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indicies = {}
        for i, num in enumerate(nums):
            req = target - num
            if req in indicies:
                return [indicies[req], i+1]
            indicies[num] = i+1
        return []