import time

def simple_timer(t):
  time.sleep(1)
  if t == 0:
    print("0\nTime's up!")
  else:
    print(t)
    simple_timer(t - 1)

simple_timer(5)