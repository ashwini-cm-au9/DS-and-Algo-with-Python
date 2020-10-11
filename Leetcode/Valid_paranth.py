class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        d={")":"(","]":"[","}":"{"}
        stack=[]
        for bracket in s:
            if bracket in d:
                if stack:
                    val=stack.pop()
                    if d[bracket]!=val:
                        return False
                else:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        else:
            return True
if __name__ == "__main__":
    s=Solution()
    print(s.isValid("()[]"))