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

# def greedy(value, weight, capacity):
#     item = media(value, weight)
#     value_max = 0
#     for i in range(len(value)):
#         if item[i][2] <= capacity:
#             value_max += item[i][1]
#             capacity -= item[i][2]
#     print(value_max)


def profit_calculate(solution, item, capacity, value, weight):
    profit = 0
    temp_item = {}
    for i in range(len(value)):
        temp_item[i] = value[i], weight[i]
    for i in range(len(solution)):
        if solution[i] == 1:
            weight = temp_item[i][1]
            capacity -= weight
            if(capacity < 0):
                return -1
            else:
                profit += temp_item[i][0]
    return profit


def local_search(solution, item, capacity, value, weight):
    best_solution = solution[:]
    begin_solution = solution[:]
    currentProfit = profit_calculate(
        begin_solution, item, capacity, value, weight)
    for i in range(len(solution)):
        if solution[i] == 1:
            solution[i] = 0
        else:
            solution[i] = 1

        neighborProfit = profit_calculate(
            solution, item, capacity, value, weight)

        if neighborProfit > currentProfit:
            currentProfit = neighborProfit
            best_solution = solution[:]

        if solution[i] == 1:
            solution[i] = 0
        else:
            solution[i] = 1
    return best_solution


def greedy_randomized_contruction(item, capacity):
    temp = item[:]
    solution_temp = []
    while len(temp) > 0:
        LCR = []
        for i in range(2):
            if len(temp) > i:
                LCR.append(temp[i])
        random_item = random.choice(LCR)

        if random_item[2] <= capacity:
            solution_temp.append(random_item[3])
            capacity -= random_item[2]

        temp.pop(temp.index(random_item))
    solution = [0 for i in range(len(item))]
    for i in solution_temp:
        solution[i] = 1

    return solution


def grasp(item, capacity, value, weight):
    best_solution = 0
    for i in range(50):
        solution = greedy_randomized_contruction(item, capacity)
        solution = local_search(solution, item, capacity, value, weight)
        best_solution = max(
            best_solution, profit_calculate(solution, item, capacity, value, weight))

    return best_solution


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

        # greedy(value, weight, capacity)
        item = media(value, weight)
        print(grasp(item, capacity, value, weight))


if __name__ == "__main__":
    main()
