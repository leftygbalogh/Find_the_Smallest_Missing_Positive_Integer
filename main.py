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
    # Write your code here

    orderNumbers = list(filter(lambda x: x > 0 and x < len(orderNumbers), orderNumbers))
    print('Filtered Ordered numbers'.format(orderNumbers))

    if len(orderNumbers) == 0:
        return 1
    orderNumbers = sorted(orderNumbers)
    print('Sorted Ordered numbers'.format(orderNumbers))
    maxNum = orderNumbers[-1]
    print('max num'.format(maxNum))


    # print(orderNumbers)
    while len(orderNumbers) > 1:
        if orderNumbers[0] >= 0 and orderNumbers[0] + 1 < orderNumbers[1]:
            return orderNumbers[0] + 1
        else:
            orderNumbers = orderNumbers[1:]
            print(orderNumbers)
    return max(maxNum + 1, 1)


if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
