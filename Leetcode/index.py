class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
if __name__ == "__main__":
    s=Solution()
    arr=[1,3,5,6]
    target=2
    print(s.searchInsert(arr,target))

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2