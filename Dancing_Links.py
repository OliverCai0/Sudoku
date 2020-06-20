import math

class Node():

    def __init__(self,right,left,up,down,head,val):
        self.right = right
        self.left = left
        self.up = up
        self.down = down
        self.head = head
        #matrix initialization purposes
        self.val = val

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_up(self):
        return self.up

    def get_down(self):
        return self.down

    def get_head(self):
        return self.head


class Col_Head(Node):

    def __init__(self,right,left,up,down,head,val,size,name):
        Node.__init__(self,right,left,up,down,head)
        self.size = size
        self.name = name


def create_initial_matrix(matrix):

    #input matrix col,row ---> made of 0s and 1s
    #column headers --> string names for requirements

    head = Node(None,None,None,None,None,None)
    curnode = head

    #establishng up and down links
    for c in range(len(matrix)):
        #column header initialization
        curnode.right = Col_Head(head,curnode,None,None,None,None,0,matrix[c][0])
        curnode = curnode.right
        c_head = curnode.right
        for r in range(1,len(matrix[c])):
            curnode.down = Node(None,None,curnode,c_head,c_head,matrix[c][r])
            if matrix[c][r] == 1:
                c_head.size += 1
            if c == 0:
                c.
            curnode = curnode.down
        curnode = curnode.head
    curnode = head

    while curnode.right != head:
        curnode = curnode.right
        c_head = curnode
        while curnode.down != c_head:
            curnode = curnode.down
            start_node = curnode
            while curnode.right != start_node:
                curnode = curnode.right

        curnode = curnode.head
        

    return head



def search(k):

    pass

def cover(col):
    col.right.left = col.left
    col.left.right = col.right
    i = col.down
    while i != col:
        j = i.right
        while j != i:
            j.down.up = j.up
            j.up.down = j.down
            j.head.size -= 1

def uncover(col):
    i = col.up
    while i != col:
        j = i.left
        while j != i:
            j.head.size += 1
            j.down.up = j
            j.up.down = j
    col.right.left = col
    col.left.right = col

