class Remove:
    def __init__(self,arr):
        self.arr=arr

    def removeDuplicates(self):
        i=0
        while(i<len(self.arr)-1):
            if self.arr[i]==self.arr[i+1]:
                del self.arr[i]
            else:
                i+=1
        return self.arr
if __name__ == "__main__":
    arr=[0,0,0,1,1,1,2,2,2]
    duplicates=Remove(arr)
    print(duplicates.removeDuplicates())

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

# It doesn't matter what values are set beyond the returned length.