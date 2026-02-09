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
        #print(buckets)

        # Distribute numbers into buckets based on current digit
        for num in arr:
            index = (num // exp) % 10
            #print("index: {index} =  number: {num} // exp {exp} % 10".format(index=index, exp=exp, num=num))
            buckets[index].append(num)
            buckets[index].append(num)
            #print (buckets)


        # Recombine buckets into the main list
        arr = [num for bucket in buckets for num in bucket]
        #print(arr)

        exp *= 10

    return arr, max_num

def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    #print(orderNumbers)

    if len(orderNumbers) == 0:
        return 1
    # orderNumbers = sorted(orderNumbers)
    orderNumbers, maxNum = radix_sort_bucket(orderNumbers)
    #orderNumbers.sort()

    #print(orderNumbers)
    while len(orderNumbers) > 1:
        if orderNumbers[0] >= 0 and orderNumbers[0]+1 < orderNumbers[1]:
            return orderNumbers[0]+1
        else:
            orderNumbers = orderNumbers[1:]
            #print(orderNumbers)
    return maxNum+1




if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
