from Dancing_Links import *
from cover_problem_version import *
import sys

if len(sys.argv) < 2:
    print('No Board(s)')
    quit()

args = sys.argv
b = open(args[1],'r')
boards = b.read().split('\n')
b.close()
bd = []
i = 0

while i < len(boards):
    if 'B' in boards[i].upper() or 'G' in boards[i].upper():
        c = 1
        curb = []
        while c <= 9:
            curb = curb + [int(i) for i in boards[i + c].split(',')]
            c += 1
        i = i + c
        bd.append(curb)
    i += 1

for board in bd:
    for i in range(9):
        print(board[i * 9:i * 9 + 9])
    print()

try:
    f = open('sudoku_cover.txt')
except IOError:
    print('Not Found, adding sudoku cover')
    create_cover_matrix()
finally:
    f.close()

head = return_dlx()
coverables = set()
#print(test_validity_constraints(head))
#print(test_val_rows(head))
for board in bd:
    for num in range(len(board)):
        if board[num] != 0:
            curnode = head.right
            while curnode.name != str(num):
                curnode = curnode.right
            print('Found match at ' + curnode.name + ' and ' + str(num))
            #print_dlx(head)
            #cover(curnode)
            coverables.add(curnode)
            d = curnode.down
            i = 1
            while i < board[num]:
                d = d.down
                i += 1
            # if d == curnode:
            #     print('Found it')
            j = d.right
            while j != d:
                #print('iter')
                # if (j.right.head == None):
                #     print('Found it')
                #     print(j.head.name)
                #cover(j.head)
                coverables.add(j.head)
                j = j.right

for col in coverables:
    cover(col)

search(head,one_answer=True,output='sudoku_answer.txt')
            



