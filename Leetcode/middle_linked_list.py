class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
class Linked_list:
    def __init__(self):
        self.head=None
    
    def addEle(self,x):
        if self.head is None:
            self.head=Node(x)
            return
        else:
            cur=self.head
            while(cur.next!=None):
                cur=cur.next
            cur.next=Node(x)
    def lenth(self):
        if self.head is None:
            return 0
        cur=self.head
        l=0
        while(cur!=None):
            l+=1
            cur=cur.next
        return l
    def middle(self):
        return self.lenth()//2

    def pri(self):
        if self.head is None:
            return 
        cur=self.head
        while(cur!=None):
            print(cur.val,end=" ")
            cur=cur.next
        print()
if __name__ == "__main__":
    link=Linked_list()
    link.addEle(1)
    link.addEle(2)
    link.addEle(3)
    link.addEle(4)
    link.pri()
    print(link.middle())
    



        