def add(x,y):
  return x+y

def multi(x, y):
  return x*y

def store(val, loc, arr):
  arr[loc] = val
  return arr

def process_vars(ops,x,y,sav,arr,log_out):
  if ops == 1:
    if log_out:
      print("Performing add on {} and {}. Saving at {}".format(arr[x], arr[y], sav))
    store(add(arr[x],arr[y]),sav,arr)
  if ops == 2:
    if log_out:
      print("Performing multi on {} and {}. Saving at {}".format(arr[x], arr[y], sav))
    store(multi(arr[x],arr[y]),sav,arr)

def runner(gravity_assist,log_out):
  opcode_pos = 0
  x_pos = 1
  y_pos = 2
  sav_pos = 3
  args = 4
  day2_target = 19690720

  while True:
    temp_ops = gravity_assist[opcode_pos]
    temp_x = gravity_assist[x_pos]
    temp_y = gravity_assist[y_pos]
    temp_sav = gravity_assist[sav_pos]
    if temp_ops == 99:
      if gravity_assist[0] == day2_target:
        print("Encountered ops code 99. Terminating with {}, noun {} and verb {}".format(gravity_assist[0],gravity_assist[1],gravity_assist[2]))
      if log_out:
        print("Encountered ops code 99. Terminating with {}, noun {} and verb {}".format(gravity_assist[0],gravity_assist[1],gravity_assist[2]))
      break
    else:
      if log_out:
        print("Working on ops {} with {} and {} locations, saving at {}".format(temp_ops, temp_x, temp_y, temp_sav))
      process_vars(temp_ops,temp_x, temp_y,temp_sav, gravity_assist, log_out)
      opcode_pos += args
      x_pos += args
      y_pos += args
      sav_pos += args

gravity_assist = []
reset_gravity_assist = []
log_out = False

with open('input1.txt') as f:
  reset_gravity_assist = list(map(int, f.read().split(',')))
  print("Input list loaded.")

for bfy in range(100):
  for bfx in range(100):
    gravity_assist = reset_gravity_assist.copy()
    gravity_assist[1] = int(bfy)
    gravity_assist[2] = int(bfx)
    try:
      runner(gravity_assist,log_out)
    except:
      print("Blew up on {},{}. Restarting...".format(bfx, bfy))
