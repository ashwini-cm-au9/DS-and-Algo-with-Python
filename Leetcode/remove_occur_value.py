class Solution:
    def removeElement(self, nums, val):
        i=0
        while(i<len(nums)):
            if nums[i]==val:
                del nums[i]
            else:
                i+=1
        return len(nums)
if __name__ == "__main__":
    arr=[3,2,2,3]
    val=3
    s=Solution()
    print(s.removeElement(arr,val))

# nums = [3,2,2,3], val = 3,

# Your function should return length = 2, with the first two elements of nums being 2.

# It doesn't matter what you leave beyond the returned length.