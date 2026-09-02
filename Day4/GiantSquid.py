randomDraws = []

boards = []

with open("input.txt", "r") as file:
    line = file.readline()
    for num in line.split(sep = ','):
        randomDraws.append(int(num))
    line = file.readline()
    while line:
        board = []
        for i in range(5):
            line = file.readline()
            board.append(list(map(int, line.split())))
        boards.append(board)
        line = file.readline()


numBoards = len(boards)
rows = len(boards[0])
cols = len(boards[0][0])

scoreBoards = [[[False for _ in range(cols)] for _ in range(rows)] for _ in range(numBoards)]

def checkBingo(scoreBoard):
    for i in range(rows):
        j = 0
        while j < cols:
            if scoreBoard[i][j] == False:
                break
            j += 1
        if j == cols:
            return True
    
    for j in range(cols):
        i = 0
        while i < rows:
            if scoreBoard[i][j] == False:
                break
            i += 1
        if i == rows:
            return True
    
    return False


def updateScore(board, scoreBoard, draw):
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == draw:
                scoreBoard[i][j] = True


def getScore(board, scoreBoard):
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if scoreBoard[i][j] == False:
                sum += board[i][j]
    return sum



def playBingo():
    for draw in randomDraws:
        for i in range(len(boards)):
            board = boards[i]
            scoreBoard = scoreBoards[i]
            updateScore(board, scoreBoard, draw)
            if checkBingo(scoreBoard):
                return draw * getScore(board, scoreBoard)
    
    return -1




def winLast():
    for draw in randomDraws:
        if len(boards) == 1:
            board = boards[0]
            scoreBoard = scoreBoards[0]
            updateScore(board, scoreBoard, draw)
            if checkBingo(scoreBoard):
                return draw * getScore(board, scoreBoard)
            continue
        indsToRemove = []
        for i in range(len(boards)):
            board = boards[i]
            scoreBoard = scoreBoards[i]
            updateScore(board, scoreBoard, draw)
            if checkBingo(scoreBoard):
                indsToRemove.append(i)

        while indsToRemove:
            ind = indsToRemove.pop()
            boards.pop(ind)
            scoreBoards.pop(ind)

    return -1


print(winLast())