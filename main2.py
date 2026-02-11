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
        while (orderNumbers[i] > 0 and #Only move a number if it is positive and
               orderNumbers[i] <= n and #if its value is smaller than the size of the list and
               orderNumbers[orderNumbers[i] - 1] != orderNumbers[i]): #the two neighbouring numbers are not equal
            print('i={}, orderNumbers[orderNumbers[i] - 1]={} != orderNumbers[i]={}'
                  .format(i, orderNumbers[orderNumbers[i] - 1], orderNumbers[i]))
            target_idx = orderNumbers[i] - 1
            print('i={}, target_idx: {} = orderNumbers[i] - 1:{}'.format(i, target_idx, orderNumbers[i] - 1
            ))
            print('Before orderNumbers[i]={}, orderNumbers[target_idx]={}'.format(orderNumbers[i], orderNumbers[target_idx]))
            orderNumbers[i], orderNumbers[target_idx] = orderNumbers[target_idx], orderNumbers[i]
            print('After orderNumbers[i]={}, orderNumbers[target_idx]={}'.format(orderNumbers[i], orderNumbers[target_idx]))

            #print(orderNumbers)

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
