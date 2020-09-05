class Paranth:

    def __init__(self,s):
        self.s=s

    def isValid(self):
        d={")":"(","}":"{","]":"["}
        stack=[]
        for char in self.s:
            if char in d:
                if stack:
                    top=stack.pop()
                else:
                    top="#"
                        
                if d[char]!=top:
                    return False
            else:
                stack.append(char)
                
        return not stack
if __name__ == "__main__":
    s="()"
    p=Paranth(s)
    print(p.isValid())
