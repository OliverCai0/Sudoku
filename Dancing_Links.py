BACKTRACKS = 0
CONSTRAINTS = 0
ROWS = 0

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

    global CONSTRAINTS
    global BACKTRACKS
    global ROWS

    CONSTRAINTS = 0
    BACKTRACKS = 0
    ROWS = 0

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
        CONSTRAINTS += 1
    print('Added ' + str(CONSTRAINTS) + ' constraints')
    return head
        
def add_row(head,row):
    global ROWS
    print('ROW ' + str(ROWS) + ' :' + row)
    #row is givn in 1..1... string format
    if not isinstance(row,str):
        print('Rows are inputted as string, with nodes represented as 1')
        return False
    if CONSTRAINTS != len(row):
        print('ROW:' + str(ROWS + 1) + ' does not match the number of constraints ' + str(CONSTRAINTS))
        return False
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
    ROWS += 1
    print('Successfully added, currently ' + str(ROWS) + ' rows')
    return True

def add_rows(head,row_array):
    for row in row_array:
        add_row(head,row)
    return True

def search(head,O = []):
    global BACKTRACKS
    print_dlx(head)
    print()

    #If R[h] = h, print the current solution and return
    if head.right == head:
        for o in range(len(O)):
            s = O[o].right
            ans = O[o].head.name + ': '
            while s != O[o]:
                ans = ans + s.head.name + ': '
                s = s.right
            print(str(o) + '. ' + ans)
        print('Backtrack number: ' + str(BACKTRACKS))
    else:
        #Otherwise choose a column object c
        curnode = head.right
        #print('Selected ' + curnode.name)
        cover(curnode)
        r = curnode.down
        count = 0
        while r != curnode:
            #print('At node ' + str(count) + ' in column ' + r.head.name)
            O.append(r)
            j = r.right
            while j != r:
                cover(j.head)
                j = j.right
            search(head,O)
            r = O.pop()
            #curnode = r.head
            j = r.left
            while j != r:
                uncover(j.head)
                j = j.left
            r = r.down
        uncover(curnode)
        BACKTRACKS += 1


    return True

def cover(col):
    #print('Covering column: ' + col.name)
    col.right.left = col.left
    col.left.right = col.right
    i = col.down
    while i != col:
        j = i.right
        while j != i:
            j.down.up = j.up
            j.up.down = j.down
            j.head.size -= 1
            j = j.right
        i = i.down
    #print('Success')

def uncover(col):
    #print('Uncovering columnn: ' + col.name)
    i = col.up
    while i != col:
        j = i.left
        while j != i:
            j.head.size += 1
            j.down.up = j
            j.up.down = j
            j = j.left
        i = i.up
    col.right.left = col
    col.left.right = col
    #print('Success')

def print_dlx(head):
    col = head.right
    while col != head:
        print(col.name + ': ' + str(col.size) + ' nodes')
        col = col.right

if __name__ == '__main__':
    t = open('DLX_test.txt','r')
    test = t.read().split('\n')
    t.close()
    print('Test Matrix')
    for line in test:
        print(line)
    print()
    print('.............................................')
    head = initialize_constraints(test[0].split(','))
    print()
    print('Printing constraint nodes, expecting:')
    for expected in ['one','two','three','four','five','six','seven']:
        print(expected + ': 0 nodes')
    print()
    print('Result:')
    print_dlx(head)
    print()
    print('.............................................')
    print()
    test = [line.replace(' ','') for line in test[1:]]
    if not add_rows(head,test):
        print()
        print('Something wrong')
        print_dlx(head)
    else:
        print()
        print('Printing current state, expecting:')
        print('one: 2 nodes')
        print('two: 2 nodes')
        print('three: 2 nodes')
        print('four: 3 nodes')
        print('five: 2 nodes')
        print('six: 2 nodes')
        print('seven: 3 nodes')
        print('.............................................')
        print_dlx(head)
        print()
        search(head)