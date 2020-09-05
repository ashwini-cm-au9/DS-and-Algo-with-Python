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
    def add_At_First(self,x):
        if self.head is None:
            self.head=Node(x)
            return
        else:
            new_node=Node(x)
            new_node.next=self.head
            self.head=new_node
    def reverse(self):
        if self.head is None:
            return
        cur=self.head
        prev=None
        while(cur!=None):
            nxt=cur.next

            cur.next=prev
            prev=cur

            cur=nxt
        self.head=prev
    def addAt_index(self,index,x):
        if self.head is None and index==0:
            self.head=Node(x)
            return
        if self.head is not None and index==0:
            new_node=Node(x)
            new_node.next=self.head
            self.head=new_node
            return
        cur=self.head
        prev=None
        idx=0
        while(cur.next!=None and idx!=index):
            prev=cur
            cur=cur.next
            idx+=1
        new_node=Node(x)
        prev.next=new_node
        new_node.next=cur
    
    def delete(self,index):
        if self.head is None:
            return
        if self.head is not None and index==0:
            self.head=self.head.next
            return
            
        cur=self.head
        prev=None
        idx=0
        while(cur.next!=None and idx!=index):
            prev=cur
            cur=cur.next
            idx+=1
        prev.next=cur.next

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
    link.addAt_index(3,10)
    link.pri()
    link.reverse()
    link.pri()
    link.delete(0)
    link.pri()