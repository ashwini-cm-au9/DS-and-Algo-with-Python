class Solution:
    def addStrings(self, num1, num2):
        n1=len(num1)
        n2=len(num2)
        
        res=[]
        carry_=0
        
        while(n1>0 or n2>0):
            if n1>0:
                num1_val=ord(num1[n1-1])-ord('0')
            else:
                num1_val=0
            if n2>0:
                num2_val=ord(num2[n2-1])-ord('0')
            else:
                num2_val=0
            
            val=(num1_val+num2_val+carry_)%10
            carry_=(num1_val+num2_val+carry_)//10
            
            res.append(val)
            
            n1-=1
            n2-=1
        if carry_:
            res.append(carry_)
        return "".join(str(i)for i in res[::-1])
if __name__ == "__main__":
    s=Solution()
    print(s.addStrings("123","123"))

#     Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

