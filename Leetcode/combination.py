#https://leetcode.com/problems/climbing-stairs/submissions/
class Solution:
    def climbStairs(self, n: int):
        result = 0
         
        for two in range(int(n/2)+1):
            one= n - 2 * two
            total = one+ two
            
            combination = math.factorial(total) / (math.factorial(two)*math.factorial(one))
            result += int(combination)
        return result
