from math import floor
from functools import reduce

result_set = []

def get_fuel(x):
  res = int(floor(x/3))-2
  if res <= 0:
    return
  else:
    result_set.append(res)
    get_fuel(res)

with open('input1.txt') as f:
  blargle = f.read().splitlines()

for x in blargle:
  get_fuel(int(x))

fuel_required = reduce((lambda x, y: x + y), result_set)

print(fuel_required)
