import sys
import math

n = int(input())
hourse = []
for i in range(n):
    pi = int(input())
    hourse.append(pi)
hourse.sort()
answer = []
for i in range(n-1):
    stre = abs(hourse[i] - hourse[i + 1])
    answer.append(stre)
print (min(answer))

