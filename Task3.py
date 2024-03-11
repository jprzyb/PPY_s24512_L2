import math
import random


def generateMatrix(x):
    m = []
    for i in range(x):
        tempList = []
        for j in range(x):
            tempList.append(getRandomValue())
        m.append(tempList)
    return m


def getRandomValue():
    x = random.uniform(0, 1)
    if x == 0:
        x += 0.0000000000000001  # the lowest float to make <0,1> to (0,1>
    return x


def showMatrix(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j], end="\t")
        print("")


def calculateNorm(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m)):
            s += m[i][j] ** 2
    return math.sqrt(s)


n = int(input("Enter the dimension of the matrix: "))
matrix = generateMatrix(n)
showMatrix(matrix)

print("### Frobenius norm: ", calculateNorm(matrix))
