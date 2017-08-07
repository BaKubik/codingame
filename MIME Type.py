import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mime_dict = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_dict[ext.lower()] = mt

for i in range(q):
    fname = input()  # One file name per line.
    filename_list = fname.split('.')
    if len(filename_list) != 1:
        print(mime_dict.get(filename_list[-1].lower(), 'UNKNOWN'))
    else:
        print("UNKNOWN")


