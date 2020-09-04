
def pri(lst):
    print(lst)
#https://www.hackerrank.com/challenges/python-lists/problem
def sortNum(lst):
    lst.sort()

def popNum(lst):
    lst.pop()

def reverse(lst):
    lst.reverse()

def insert(lst,x,y):
    lst.insert(x,y)

def remov(lst,x):
    lst.remove(x)

def append(lst,x):
    lst.append(x)

if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        inp=input().split(" ")
        if inp[0]=="print":
            pri(lst)
        if inp[0]=="sort":
            sortNum(lst)
        if inp[0]=="pop":
            popNum(lst)

        if inp[0]=="reverse":
            reverse(lst)
        if inp[0]=="insert":
            insert(lst,int(inp[1]),int(inp[2]))
        if inp[0]=="remove":
            remov(lst,int(inp[1]))
        if inp[0]=="append":
            append(lst,int(inp[1]))
