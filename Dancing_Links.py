class Node():

    def __init__(self,right,left,up,down,head):
        self.right = right
        self.left = left
        self.up = up
        self.down = down
        self.head = head


class Col_Head(Node):

    def __init__(self,right,left,up,down,head,size,name):
        Node.__init__(self,right,left,up,down,head)
        self.size = size
        self.name = name

def initialize_constraints(constraints):
    head = Node(None,None,None,None,None)
    head.right = head
    head.left = head
    for c in range(len(constraints)):
        if c == 0:
            curnode = Col_Head(None,None,None,None,None,0,constraints[c])
            head.right = curnode
            head.right.left = head
        else:
            curnode.right = Col_Head(None,curnode,None,None,None,0,constraints[c])
            curnode = curnode.right
        if c == len(constraints) - 1:
            curnode.right = head
            curnode.right.left = curnode
    return head
        
def add_row(head,row):
    #row is givn in 1..1... string format
    cur_col = head
    nodes_added = []
    for i in range(len(row)):
        cur_col = cur_col.right
        if row[i] == '1':
            if not cur_col.down:
                cur_col.down = Node(None,None,cur_col,cur_col,cur_col)
                cur_col.up = cur_col.down
                nodes_added.append(cur_col.down)
            else:
                cur_col.up.down = Node(None,None,cur_col.up,cur_col,cur_col)
                cur_col.up = cur_col.up.down
                nodes_added.append(cur_col.up)
            cur_col.size += 1
    for i in range(len(nodes_added)):
        if i == 0:
            nodes_added[i].left = nodes_added[-1]
            nodes_added[i].left.right = nodes_added[i]
        else:
            nodes_added[i].left = nodes_added[i - 1]
            nodes_added[i].left.right = nodes_added[i]
        


def search(head):

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

def print_dlx(head):
    cols = head
    col_count = 0
    
    while cols.right != head:
        print(cols.right.name + ' : ' + cols.right.size)
        col_count += 1
        cols = cols.right
