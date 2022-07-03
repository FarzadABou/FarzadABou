import math

k = int(input())

for i in range(1, 10**9):
    if 0 <= math.sin(i) <= 1/k:
        print(i)
        exit()
 #  creat by farzadAB . . . . . . . . . . . . . . .
