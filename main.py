import random
#приложения грф интерфейс

import numpy as np

class Child(object):
    def __init__(self, name, sex, expass, history, graph, math, chemistry, phisycs, scholarship):
        self.name = name
        self.sex = sex
        self.expass = expass
        self.history = history
        self.graph = graph
        self.math = math
        self.chemistry = chemistry
        self.phisycs = phisycs
        self.scholarship = scholarship

    def printChild(self):
        return "%s %s %s %s %s %s %s %s %s" % (self.name, self.sex, self.expass, self.history, self.graph, self.math, self.chemistry, self.phisycs, self.scholarship)

v = 0.30
Rk = 1

N = 9
M = 20
x_0 = np.reshape(np.zeros((N-1)*M), (M, (N-1)))
i = 0
objectsChild = []
with open('input.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        x_start = line.replace('\n', '').split(' ')
        child = Child(x_start[0], x_start[1], x_start[2], x_start[3], x_start[4], x_start[5], x_start[6], x_start[7], x_start[8])
        objectsChild.append(child.printChild())
        for j in range(len(x_start)-1):
            x_0[i][j] = x_start[j+1]
        i += 1

#Нормализация выборки
b = x_0.transpose()
x = np.reshape(np.zeros((N-2)*M), (M, N-2))
for i in range(M):
    for j in range(N-2):
        x[i][j] = np.round((x_0[i][j] - min(b[j])) / (max(b[j]) - min(b[j])), 2)
#Первые кластеры
count = 0 #Количество кластеров
w = np.reshape(np.zeros((N-2)*M), (M, (N-2)))
w[0] = x[0]
for i in range(M):
    R = np.zeros(count+1)
    for j in range(count+1):
        for k in range(N-2):
            R[j] += np.power(x[i][k] - w[j][k], 2)
        R[j] = np.sqrt(R[j])
    bestR = min(R)
    if bestR <= Rk:
        bestR = list(R).index(bestR)
        for j in range(N - 2):
            w[bestR][j] += v * (x[i][j] - w[bestR][j])
    else:
        count += 1
        w[count] = x[i]

# w = np.array([[0.2, 0.2, 0.3, 0.4, 0.4, 0.2, 0.5],
#               [0.2, 0.8, 0.7, 0.8, 0.7, 0.7, 0.8],
#               [0.8, 0.2, 0.5, 0.5, 0.4, 0.4, 0.4],
#               [0.8, 0.8, 0.6, 0.7, 0.7, 0.6, 0.7]])

ChildForClasters = ['']*(count+1)
    # np.reshape(np.array(' ' * 1 * (count+1)), (count+1, 1)).tolist()

steps = 6
for z in range(steps):
    v = 0.3 - 0.05*z
    listforstep = list(range(1, 21))
    random.shuffle(listforstep)
    for i in range(M):
        R = np.zeros(count+1)
        number = listforstep[i]-1
        for j in range(count+1):
            for k in range(N-2):
                R[j] += np.power(x[number][k] - w[j][k], 2)
            R[j] = np.sqrt(R[j])
        bestR = min(R)
        bestR = list(R).index(bestR)
        for j in range(N-2):
            w[bestR][j] += v * (x[number][j] - w[bestR][j])


for i in range(M):
    R = np.zeros(count+1)
    for j in range(count+1):
        for k in range(N-2):
            R[j] += np.power(x[i][k] - w[j][k], 2)
        R[j] = np.sqrt(R[j])
    bestR = min(R)
    bestR = list(R).index(bestR)
    ChildForClasters[bestR] += '%s ' % (i+1)


for i in range(len(ChildForClasters)):
    num = i+1
    print("В " + str(num) + " кластер")
    numChild = ChildForClasters[i]
    numChild = numChild.split(' ')
    for j in range(len(numChild)-1):
        number = int(numChild[j])-1
        print("№" + str(number+1) + " " + objectsChild[number])
