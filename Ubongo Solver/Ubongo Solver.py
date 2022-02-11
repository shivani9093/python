import numpy as np

# defining board and pieces

board = np.array([[1,1,1,-1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]])

piece_1 = np.array([[2,1,1,1],
                    [2,1,1,1],
                    [2,1,1,1],
                    [1,1,1,1]])

piece_2 = np.array([[3,3,1,1],
                    [3,3,1,1],
                    [1,1,1,1],
                    [1,1,1,1]])

piece_3 = np.array([[1,4,1,1],
                    [4,4,1,1],
                    [1,1,1,1],
                    [1,1,1,1]])

piece_4 = np.array([[5,5,1,1],
                    [5,1,1,1,],
                    [5,1,1,1],
                    [5,1,1,1]])


# possible rearrangement of all 4 pieces

arrange_p1 = [piece_1]
for i in range(7):
    piece_1 = (np.roll(piece_1,1))
    arrange_p1.append(piece_1)
    
arrange_p2 = [piece_2]
shift = 1
for i in range(2):
    piece_2 = (np.roll(piece_2,1,axis=1))
    arrange_p2.append(piece_2)
    piece_2 = (np.roll(piece_2,1,axis=1))
    arrange_p2.append(piece_2)
    for k in range(1):
        piece_2 = (np.roll(arrange_p2[0],shift,axis=0))
        if shift<=2:
            arrange_p2.append(piece_2)
        shift+=1
        
arrange_p3 = [piece_3]
shift = 1
for i in range(3):
    piece_3 = (np.roll(piece_3,1,axis=1))
    arrange_p3.append(piece_3)
    piece_3 = (np.roll(piece_3,1,axis=1))
    arrange_p3.append(piece_3)
    for z in range(1):
        piece_3 = (np.roll(arrange_p3[0],shift,axis=0))
        if shift<=2:
            arrange_p3.append(piece_3)
        shift+=1

arrange_p4 = [piece_4]
for i in range(3):
    piece_4 = (np.roll(piece_4,1,axis=1))
    arrange_p4.append(piece_4)
    piece_4 = (np.roll(piece_4,1,axis=1))
    arrange_p4.append(piece_4)
    for y in range(1):
        piece_4 = (np.roll(arrange_p4[0],3,axis=0))
        arrange_p4.append(piece_4)


# possible rotations and unique combinations of all 4 pieces

def rotation_and_unique(arrange_p):
    rotated_p = []
    piece_no = 0
    while piece_no in range(len(arrange_p)):
        for p in range(4):
            arrange_p[piece_no] = (np.rot90(arrange_p[piece_no]))
            rotated_p.append(arrange_p[piece_no])
        piece_no+=1

    unique_p = []
    for i in rotated_p:
        if not any(np.array_equal(i, temp) for temp in unique_p):
            unique_p.append(i)
    return unique_p

unique_p1 = rotation_and_unique(arrange_p1)       
unique_p2 = rotation_and_unique(arrange_p2)
unique_p3 = rotation_and_unique(arrange_p3)
unique_p4 = rotation_and_unique(arrange_p4)       


# function to check if game is solved
 
def check(answer):
    
    m,n = np.shape(board)
    
    puzzle = True
    for i in range(m):
        if puzzle == False:
            break
        for j in range(n):
            if answer[i][j]==1 or answer[i][j]>5:
                puzzle=False
                break
            if board[i][j]==-1 and answer[i][j]!=-1:
                puzzle=False
                break     
        
    if puzzle == True:
        return puzzle


# adding the pieces to board 

num = 0
for q in range(len(unique_p1)):
    for w in range(len(unique_p2)):
        for e in range(len(unique_p3)):
            for r in range(len(unique_p4)):
                soln = board*unique_p1[q]*unique_p2[w]*unique_p3[e]*unique_p4[r]
                if check(soln):
                    num+=1
                    print('UBONGO !!')
                    print(f'{num}TH soln--->')
                    print(soln)
                    print('\n')