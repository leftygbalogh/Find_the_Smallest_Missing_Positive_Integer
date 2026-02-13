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

    orderNumbers = list(set(orderNumbers))
    #A set is an ordered, deduplicated list, turning a noisy, dirty list into a cleaner one
    orderNumbers = list(filter(lambda x: 0 < x <= len(orderNumbers) , orderNumbers))
    #The lambda filter removes all values that are out of range,
    # so even in worst case scenario, there are only len(orderNumbers)

    for i in range(len(orderNumbers)):
        if orderNumbers[i] != i+1:
            return i + 1
    return len(orderNumbers) + 1

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
