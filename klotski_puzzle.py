import sys
sys.setrecursionlimit(100000)

print(sys.getrecursionlimit())

'''
Class block, which is used to define our blocks and gice properties to them
'''
class Block:
    def __init__(self, x, y, color, code):
        self.x = x
        self.y = y
        self.color = color
        self.code = code


'''
Method to generate a new game board, everytime we change the position of a block
'''
def printGameBoard(blocks):
    for x in range(5):
        for y in range(4):
            gameBoard[x][y] = 'XX'

    for block in blocks:
        if block.color == 'blue':
            gameBoard[block.x][block.y] = block.code
            gameBoard[block.x + 1][block.y] = block.code
        elif block.color == 'pink':
            gameBoard[block.x][block.y] = block.code
            gameBoard[block.x][block.y+1] = block.code
        elif block.color == 'green':
            gameBoard[block.x][block.y] = block.code
        elif block.color == 'red':
            gameBoard[block.x][block.y] = block.code
            gameBoard[block.x + 1][block.y] = block.code
            gameBoard[block.x][block.y + 1] = block.code
            gameBoard[block.x + 1][block.y + 1] = block.code



    print(np.matrix(gameBoard))

'''
Method to check if the neighbour is suitable for this particular block.
'''
def neighbourIsSuitable(block, i, j):
    suitable = False
    indentedI = i+1
    indentedJ = j+1
    if block.color == 'blue':
        if gameBoard[i][j] == 'XX' or gameBoard[i][j] == block.code:
            if indentedI < 5:
                if gameBoard[indentedI][j] == 'XX' or gameBoard[indentedI][j] == block.code:
                    suitable = True
    elif block.color == 'pink':
        if gameBoard[i][j] == 'XX' or gameBoard[i][j] == block.code:
            if indentedJ < 4:
                if gameBoard[i][indentedJ] == 'XX' or gameBoard[i][indentedJ] == block.code:
                    suitable = True
    elif block.color == 'green':
#         print("IN GREEN "+block.code)
#         print("i is "+str(i)+" j is "+str(j)+" and gameboardIJ is "+gameBoard[i][j])
#         print(np.matrix(gameBoard))
        if gameBoard[i][j] == 'XX':
            suitable = True
    elif block.color == 'red':
        if gameBoard[i][j] == 'XX' or gameBoard[i][j] == block.code:
            if indentedI < 5:
                if indentedJ < 4:
                    if gameBoard[i][indentedJ] == 'XX' or gameBoard[i][indentedJ] == block.code:
                        if gameBoard[indentedI][j] == 'XX' or gameBoard[indentedI][j] == block.code:
                            if gameBoard[indentedI][indentedJ] == 'XX' or gameBoard[indentedI][indentedJ] == block.code:
                                suitable = True
    return suitable


'''
Method which checks and returns the indexes of the empty neighbours of a block
'''
def checkEmptyNeighbours(block):
    array = []
    iIndex = 0
    count = 0

    for i in range(block.x-1, block.x+2):
        for j in range(block.y-1, block.y+2):
            if count % 2 != 0 and i >= 0 and i <= 4 and j >= 0 and j <= 3:
                if neighbourIsSuitable(block, i, j):
                    array.append([i, j])

            count += 1
    return array

'''
Method to generate a new pattern, if a block is moved to a new position
'''
def getPattern(block, neighbourX, neighbourY):
    newPattern = [[0 for x in range(4)]for y in range(5)]

    for x in range(5):
        for y in range(4):
            newPattern[x][y] = 'XX'

    for b in blocks:
        if(b != block):
            newPattern[b.x][b.y] = b.color
        else:
            newPattern[neighbourX][neighbourY] = block.color

    return newPattern


'''
Method to see if a block can move to a particular position or not
'''
def canMove(block, neighbourX, neighbourY):
    patternFound = False
#     print()
#     print()
#     print('neighbourX is '+str(neighbourX)+' neighbourY is '+ str(neighbourY))
    newPattern = getPattern(block, neighbourX, neighbourY)
#     print(' New Pattern is ')
#     print(np.matrix(newPattern))

    if len(patterns) == 0:
        patterns.append(newPattern)
    else:
        if newPattern in patterns:
#             print('pattern found Bitch, returning false!')
            return False
        else:
            patterns.append(newPattern)
#             print('pattern not found, appending and returning true!')
            return True;


'''
Main method to solve the puzzzle
'''
def solve():
    global solved
    if not solved:
        if redOne.x == 3 and redOne.y == 1:
            print('\n')
            print("PUZZLE SOLVED! red has reached 3, 1 exit program!")
            solved = True
        global solveCalled
        solveCalled = solveCalled + 1
        print('\n')
        print('\n')
        print('solve called : ' + str(solveCalled))
        for block in blocks:
            emptyNeighbours = checkEmptyNeighbours(block)
#             print(block.code)
#             print(emptyNeighbours)
            for neighbour in emptyNeighbours:
                neighbourX = neighbour[0]
                neighbourY = neighbour[1]
#                 print('neighbourX is ' + str(neighbourX) + ' neigbourY is ' + str(neighbourY) )
                if canMove(block, neighbourX, neighbourY) and not solved:

                    print(block.code + ' is moving to ' + str(neighbourX) + ' ' + str(neighbourY))
                    print('\n')
                    block.x = neighbourX
                    block.y = neighbourY
                    printGameBoard(blocks)
                    solve()



'''
Start of the program where variables etc. are initialised
'''
gameBoard = [[0 for x in range(4)]for y in range(5)]
import numpy as np
blueOne = Block(0, 0, 'blue', 'B1')
blueTwo = Block(0, 3, "blue", 'B2');
blueThree = Block(2, 0, "blue", 'B3');
blueFour = Block(2, 3, "blue", 'B4');
pinkBlock = Block(2, 1, "pink", 'P1');
greenOne = Block(3, 1, "green", 'G1');
greenTwo = Block(3, 2, "green", 'G2');
greenThree = Block(4, 0, "green", 'G3');
greenFour = Block(4, 3, "green", 'G4');
redOne = Block(0, 1, 'red', 'R1')

blocks = [

    redOne,
    greenOne,
    greenTwo,
    greenThree,
    greenFour,
    pinkBlock,
    blueOne,
    blueTwo,
    blueThree,
    blueFour,
  ]

print("Here is the initial game board!")
printGameBoard(blocks)
patterns = []
solveCalled = 0
solved = False

'''
Calling the solve method
'''
solve()


print("Total number of steps : " + str(solveCalled))
