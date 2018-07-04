# Завдання 4. 
# Дано товарний чек. В ньому знаходяться товари, кількість та ціна. Підсумок чеку містить розрахунок податку.
# Ваша задача скорелювати розрахунок податку на одну позицію в чеку так, щоб в підсумок податків на кожну позицію
# дорівнював загальному підсумку. Точність виведення два знаки після коми.

# prices_n_quantities = [[price_1, quantity_1], [price_2, quantity_2], [price_3, quantity_3],
#                        [price_4, quantity_4], [price_5, quantity_5], [price_6, quantity_6],
#                        [price_7, quantity_7], [price_8, quantity_8], [price_9, quantity_9]]

import numpy as np
from functools import reduce

start_set = [[397.01, 1], [435.0, 2], [435.0, 2], [443.33, 2], [443.33, 2],
                       [370.0, 2], [630.0, 1], [630.0, 1], [630.0, 2]]


def tax_calc(tax_percent, tax_total_given, prices_n_quantities):
    
    table = np.array(prices_n_quantities)
    products = table.shape[0]
    tax_divided = []
    
    for x in range(0, products):
        tax_divided.append(table[x][0] * table[x][1] * tax_percent / 100)
    tax_total = reduce((lambda x, y: x + y), tax_divided)
    
    tax_divided_rounded = list(map(lambda x: round(x, 2), tax_divided))
    tax_total_rounded = reduce((lambda x, y: x + y), tax_divided_rounded)
    
    # Defining the difference caused by rounding
    diff = tax_total_given - tax_total_rounded
    round_diff = [round(x - y, 3) for x, y in zip(tax_divided, tax_divided_rounded)]
    max_round_diff = max(round_diff)

    # Selecting, what element to change in an opposite direction
    max_round_diff_maximal = 0
    max_round_diff_maximal_position = 0
    for x in range(0, len(round_diff)):
        if round_diff[x] == max_round_diff and tax_divided[x] > max_round_diff_maximal:
            max_round_diff_maximal = tax_divided[x]
            max_round_diff_maximal_position = x

    # Amending...
    tax_divided_rounded[max_round_diff_maximal_position] += diff
    tax_total_rounded = reduce((lambda x, y: x + y), tax_divided_rounded)
    
    return tax_divided_rounded
print(tax_calc(20, 1434.07, start_set))