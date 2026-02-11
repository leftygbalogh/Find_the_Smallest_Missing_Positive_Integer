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

def radix_sort_bucket(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        # print(buckets)

        # Distribute numbers into buckets based on current digit
        for num in arr:
            if num < 0:
                pass
            else:
                index = (num // exp) % 10
                buckets[index].append(num)
                buckets[index].append(num)

        # Recombine buckets into the main list
        arr = [num for bucket in buckets for num in bucket]
        # print(arr)

        exp *= 10

    return arr, max_num

def countSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

    return arr, max_val



def findSmallestMissingPositive(orderNumbers):
    # Write your code here

    if len(orderNumbers) == 0:
        return 1
    # orderNumbers = sorted(orderNumbers)
    #orderNumbers, maxNum = radix_sort_bucket(orderNumbers) #3 9 12
    orderNumbers, maxNum = countSort(orderNumbers)

    # orderNumbers.sort()
    #orderNumbers = list(set(orderNumbers))
    #orderNumbers = sorted(orderNumbers) #3 9 12
    #maxNum = orderNumbers[-1]           #3 9 12


    # print(orderNumbers)
    while len(orderNumbers) > 1:
        if orderNumbers[0] >= 0 and orderNumbers[0] + 1 < orderNumbers[1]:
            return orderNumbers[0] + 1
        else:
            orderNumbers = orderNumbers[1:]
            # print(orderNumbers)
    return max(maxNum + 1, 1)


if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
