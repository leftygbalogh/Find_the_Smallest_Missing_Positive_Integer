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
    #print(orderNumbers)
    if len(orderNumbers) == 0:
        return 1
    orderNumbers = sorted(orderNumbers)
    base = orderNumbers[0]
    for index in range(1, len(orderNumbers)):

        #print(f"index {index};  sortedOrderNumbers: {sortedOrderNumbers[index]}")
        if orderNumbers[index] >= 0 and base+index < orderNumbers[index]:
            return base + 1
        base = orderNumbers[index]
    return max(orderNumbers) + 1



if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
