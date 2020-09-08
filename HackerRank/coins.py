class Solution:
    def solve(self,n,idx):
        if idx==n:
           return 1
        if idx>n:
            return 0
        else:
            return self.solve(n,idx+1)+self.solve(n,idx+2)

    def climbStairs(self, n):
        print(self.solve(n,1))
        
if __name__ == "__main__":
    s=Solution()
    s.climbStairs(3)