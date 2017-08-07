import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(",", "."))
lat = float(input().replace(",", "."))
n = int(input())
defib_list = []

closer = 999999999999999999
adr_cord = -1
for i in range(n):
    defib = input().split(";")

    adr = defib[1]
    x = float(defib[-2].replace(",", "."))
    y = float(defib[-1].replace(",", "."))
    defib_list.append(adr)

    def_x = (x - lon) * math.cos(lat / 2 + y / 2)
    def_y = y - lat
    d = math.sqrt((def_x * def_x) + (def_y * def_y)) * 6371
    if closer > d:
        closer = d
        adr_cord = i

print(defib_list[adr_cord])