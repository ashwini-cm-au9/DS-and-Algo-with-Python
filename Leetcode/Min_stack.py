#https://leetcode.com/problems/min-stack/submissions/
class MinStack:

    def __init__(self):
        self._stack=[]
        self._stack2=[]
        
    def push(self, x: int) -> None:
        self._stack.append(x)
        if len(self._stack2)==0:
            self._stack2.append(x)
        else:
            y=self._stack2[-1]
            if y>x:
                self._stack2.append(x)
            else:
                self._stack2.append(y)
            
    def pop(self) -> None:
        if len(self._stack)>0 and len(self._stack2)>0:
            self._stack.pop()
            self._stack2.pop()
    
    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        if len(self._stack2)>0:
            return self._stack2[-1]
        else:
            return -1
