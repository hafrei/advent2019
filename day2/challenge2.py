def add(x,y):
  return x+y

def multi(x, y):
  return x*y

def store(val, loc, arr):
  arr[loc] = val
  return arr

def stop_code(ops):
  assume_false = False
  if ops == 99:
    assume_false = True
  return assume_false

def process_vars(ops,x,y,sav,arr):
  if ops == 1:
    print("Performing add on {} and {}. Saving at {}".format(arr[x], arr[y], sav))
    store(add(arr[x],arr[y]),sav,arr)
  if ops == 2:
    print("Performing multi on {} and {}. Saving at {}".format(arr[x], arr[y], sav))
    store(multi(arr[x],arr[y]),sav,arr)

gravity_assist = []
is_stop = False
opcode_pos = 0
x_pos = 1
y_pos = 2
sav_pos = 3

with open('input1.txt') as f:
  gravity_assist = list(map(int, f.read().split(',')))
  print("Input list loaded.")

while is_stop == False:
  temp_ops = gravity_assist[opcode_pos]
  temp_x = gravity_assist[x_pos]
  temp_y = gravity_assist[y_pos]
  temp_sav = gravity_assist[sav_pos]
  is_stop = stop_code(temp_ops)
  if is_stop:
    print("Encountered ops code 99. Terminating with {}".format(gravity_assist[0]))
    break
  else:
    print("Working on ops {} with {} and {} locations, saving at {}".format(temp_ops, temp_x, temp_y, temp_sav))
    process_vars(temp_ops,temp_x, temp_y,temp_sav, gravity_assist)
    opcode_pos += 4
    x_pos += 4
    y_pos += 4
    sav_pos += 4
