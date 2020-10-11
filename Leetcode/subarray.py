class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        cur=nums[0]
        total=nums[0]
        for i in range(1,len(nums)):
            if cur+nums[i]>nums[i]:
                cur=cur+nums[i]
            else:
                cur=nums[i]
            if cur>total:
                total=cur
                
        return total
if __name__ == "__main__":
    s=Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
