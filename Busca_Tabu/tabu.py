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


# preciso pegar o maior dos valores do ente o vizinho
def local_search(solution, item, capacity, value, weight):
    best_solution = solution[:]
    current_profit = profit_calculate(solution, item, capacity, value, weight)
    temp_profit = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            solution[i] = 0
        else:
            solution[i] = 1

        temp_profit = profit_calculate(
            best_solution, item, capacity, value, weight)

        if(temp_profit >= current_profit):
            current_profit = temp_profit
            T = i
            final_solution = solution[:]
            final_profit = temp_profit

        if solution[i] == 1:
            solution[i] = 0
        else:
            solution[i] = 1

    return final_solution


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


def tabu(item, capacity, value, weight):
    profit = []
    bt_max = 2
    T = []
    acc = 0
    for i in range(25):
        solution = greedy_randomized_contruction(item, capacity)
        acc = 0
        while acc <= bt_max:

            solution = local_search(solution, item, capacity, value, weight)
            if(solution not in T):
                T.append(solution)
                profit.append(profit_calculate(
                    solution, item, capacity, value, weight))
            acc = acc + 1
        #temp = max(profit)
        #ind = profit.index(temp)

    return max(profit)


def main():
    for it in range(6):
        file = open("entradas/input"+str(it+11)+".in", "r")
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
        print(tabu(item, capacity, value, weight))


if __name__ == "__main__":
    main()
