import re
import random
import numpy as np
from operator import itemgetter


def media(value, weight):
    item = {}
    for i in range(len(value)):
        item[i] = np.divide(value[i], weight[i]), value[i], weight[i], i

    item = sorted(item.values(), reverse=True)

    return item


def greedy(value, weight, capacity):
    item = media(value, weight)
    value_max = 0
    for i in range(len(value)):
        if capacity == 0:
            break
        if item[i][2] <= capacity:
            value_max += item[i][1]
            capacity -= item[i][2]
    print(value_max)


def main():
    for it in range(16):
        file = open("entradas/input"+str(it+1)+".in", "r")
        i = 1
        n = None
        capacity = None
        item = []
        value = []
        weight = []
        for line in file:
            if i == 1:
                n = int(line)
            elif 1 < i <= n+1:
                s = str(line)
                aux1, aux2, aux3 = s.split()
                item.append(int(aux1))
                value.append(int(aux2))
                weight.append(int(aux3))
            else:
                capacity = int(line)
            i += 1

        greedy(value, weight, capacity)


if __name__ == "__main__":
    main()
