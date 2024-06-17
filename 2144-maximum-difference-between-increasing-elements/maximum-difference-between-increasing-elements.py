class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m=0
        k=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    k=nums[j]-nums[i]
                    if k>=m:
                        m=k
        if m==0:
            return -1
        return m