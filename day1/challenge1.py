from math import floor
from functools import reduce

result_set = []

with open('input1.txt') as f:
  blargle = f.read().splitlines()

for x in blargle:
  res = floor(int(x)/3)-2
  result_set.append(res)

fuel_required = reduce((lambda x, y: x + y), result_set)

print(fuel_required)
