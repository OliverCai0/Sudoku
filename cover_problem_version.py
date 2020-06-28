from Dancing_Links import *

def create_cover_matrix():
    box_num = '.' * 81

    rows = [list(range(i * 9,i * 9 +9)) for i in range(9)]
    columns = [list(range(i,i + 73,9)) for i in range(9)]
    neighbors = ([[0 + i * 3, 1 + i * 3, 2 + i * 3,
                  9+ i * 3,10+ i * 3,11+ i * 3,
                  18+ i * 3,19+ i * 3,20+ i * 3] for i in range(3)
                  ] + 
                  [[27 + i * 3,28 + i * 3,29 + i * 3,
                    36 + i * 3,37 + i * 3,38 + i * 3,
                    45 + i * 3,46 + i * 3,47 + i * 3] for i in range(3)
                  ] + 
                  [[54 + i * 3,55 + i * 3,56 + i * 3,
                    63 + i * 3, 64 + i * 3, 65 + i * 3,
                    72 + i * 3, 73 + i * 3, 74 + i * 3] for i in range(3)])
    sudoku = open('sudoku_cover.txt','w')
    print('Hello')
    for i in range(0,81):
        for num in range(0,9):
            sudoku.write(box_num[:i] + '1' + box_num[i + 1:])
            for n in range(len(rows)):
                if i in rows[n]:
                    sudoku.write(box_num[:n * 9 + num] + '1' + box_num[n * 9 + num + 1:])
                    break
            for n in range(len(columns)):
                if i in rows[n]:
                    sudoku.write(box_num[:n * 9 + num] + '1' + box_num[n * 9 + num + 1:])
                    break
            for n in range(len(neighbors)):
                if i in rows[n]:
                    sudoku.write(box_num[:n * 9 + num] + '1' + box_num[n * 9 + num + 1:])
                    break
            if not (i == 80 and num == 8):
                sudoku.write('\n')
            else:
                print('exception')
                print(i)
                print(n)
            #row1: 0-8,9-17
            #column1: 0,9,18...72 : 1,10
            #neighbor1: 0,1,2,9,10,11,18,19,20
    sudoku.close()

def return_dlx():
    sudoku_constraints = ([(str(i)) for i in range(0,81)] + 
                      [('r' + str(i % 9)) for i in range(0,81)] + 
                      [('c'  + str(i % 9)) for i in range(0,81)] + 
                      [('n' + str(i % 9)) for i in range(0,81)])

    head = initialize_constraints(sudoku_constraints)
    s = open('sudoku_cover.txt','r')
    sudoku = s.read().split('\n')
    add_rows(head,sudoku)
    s.close()

    print('Success')
    return head

if __name__ == '__main__':
    create_cover_matrix()
    print_dlx(return_dlx())
