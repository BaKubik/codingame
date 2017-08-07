import sys
import math

message = (input())

clear_binary = ''
answer = ''

for char in message:
    binary = (bin(ord(char))[2:])

    while len(binary) < 7:
        binary = '0' + binary
    clear_binary += binary

lastDeg = ""
count = 0
for deg in clear_binary:
    if deg == lastDeg:
        count += 1
    else:
        if lastDeg == '0':
            answer += '00 '
        elif lastDeg == '1':
            answer += '0 '
        for i in range(count):
            answer += '0'
        if count > 0:
            answer += ' '

        lastDeg = deg
        count = 1

if lastDeg == '0':
    answer += '00 '
elif lastDeg == '1':
    answer += '0 '
for i in range(count):
    answer += '0'

print(answer)