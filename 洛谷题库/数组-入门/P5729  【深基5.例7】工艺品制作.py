w, x, h = map(int,input().split())
q = int(input())
board = [[[0] * (h + 1) for _ in range(x + 1)] for _ in range(w + 1)]
print(board)
for _ in range(q):
    x1, y1, z1, x2, y2, z2 = map(int,input().split())
    for i in range(x1,x2 + 1):
        for j in range(y1,y2 + 1):
            for k in range(z1,z2 + 1):
                board[i][j][k] = 1

count = 0
for i in range(1,w + 1):
    for j in range(1,x + 1):
        for k in range(1,h + 1):
            if board[i][j][k] == 0:
                count += 1
print(count)