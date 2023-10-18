

counter = 0
def canBePlaced(n, row, col, arr):
    newArr = []
    newArr = arr[row].copy()
    if 1 in newArr:
        return False
    newArr.clear()
    for i in range(n):
        if col < n:
            newArr.append(arr[i][col])
    if 1 in newArr:
        return False
    newArr.clear()
    temprow = row
    tempcol = col
    while temprow + 1 < n and tempcol > 0:
        newArr.append(arr[temprow+1][tempcol-1])
        temprow += 1
        tempcol -= 1
    if 1 in newArr:
        return False
    temprow = row
    tempcol = col
    while temprow > 0 and tempcol > 0:
        newArr.append(arr[temprow-1][tempcol-1])
        temprow -= 1
        tempcol -= 1
    if 1 in newArr:
        return False
    return True
def nQueens(n, row, col, arr):
    if col == n:
        global counter
        counter += 1
    for i in range(n):
        # row = i
        if canBePlaced(n, i, col, arr): #if it can be placed at the given row and column num, return true, else return false
            arr[i][col] = 1
            nQueens(n, i, col + 1, arr)
            arr[i][col] = 0
        #use for loop to try each row in the given column or value of n
        #for each row, if valid, place queen, make recursive call, remove most recent queen

if __name__ == '__main__':
    input = open("input.txt")
    n = int(input.readline())
    arr = [[0] * n for _ in range(n)]
    row = 0
    col = 0
    nQueens(n, row, col, arr)
    result = counter
    with open("output.txt", "a") as f:
        f.write(str(result) + '\n')

    input.close()