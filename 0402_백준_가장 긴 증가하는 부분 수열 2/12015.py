import sys
sys.stdin = open('sample.txt', 'r')

import bisect
N = int(input())
sequence = list(map(int, input().split()))
tail = []
for i in sequence:
    idx = bisect.bisect_left(tail, i)
    
    if idx == len(tail):
        tail.append(i)
    else:
        tail[idx] = i
        
print(len(tail))
