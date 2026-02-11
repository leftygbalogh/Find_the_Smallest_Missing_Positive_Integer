#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#
def findSmallestMissingPositive(orderNumbers):
    if len(orderNumbers) == 0:
        return 1

    n = len(orderNumbers)
    for i in range(n):
        while 1 <= orderNumbers[i] <= n and orderNumbers[orderNumbers[i] - 1] != orderNumbers[i]:
            target_idx = orderNumbers[i] - 1
            orderNumbers[i], orderNumbers[target_idx] = orderNumbers[target_idx], orderNumbers[i]

    for i in range(n):
        if orderNumbers[i] != i + 1:
            return i + 1

    return n + 1

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
