
import math
import os
import random
import re
import sys

def longestSubarray(arr):
    left=0
    right=0
    ar1=[]
    c1=0
    count=0
    while(right<len(arr)):
        if ar1==[]:
            smallest=arr[left]
            ar1.append(arr[right])
            right+=1
            c1+=1
        elif arr[right] in ar1:
            c1+=1
            right+=1
        elif arr[right] not in ar1 and len(ar1)<2 and (abs(arr[right]-smallest)<2):
            ar1.append(arr[right])
            right+=1
            c1+=1
        else:
            count=max(count,c1)
            c1=0
            left+=1
            right=left
            ar1=[]
        if right==len(arr):
            count=max(count,c1)
    print(count)


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)
    
