1.Make bricks:
def make_bricks(small, big, goal):
 diff = (goal-big*5)
  if diff > 0:
    if small >= diff:
      return True
    else:
      return False
  elif diff == 0:
    return True
  else:
    div = round((big*5)/goal)
    remain = abs((div*5) - goal)
    if small < remain:
      return False
    else:
      return True

def make_bricks(small, big, goal):
  if (goal > (big*5 + small)): 
    return False
  elif ((goal % 5) > small): 
    return False
  else:
    return True;
---------------------------------------------------

2.lone_sum:
def lone_sum(a, b, c):
  if (a==b) and (b==c):
    return 0
  elif (a!=b) and (b!=c) and (a!=c):
    return (a+b+c)
  else:
    if b==c:
      return a
    elif a==c:
      return b
    else:
      return c;
---------------------------------------------------
3.Lucky sum:
def lucky_sum(a, b, c):
  
  if a==13:
    return 0
  elif b==13:
    return a
  elif c==13:
    return (a+b)
  else:
    return (a+b+c)
---------------------------------------------------
4.No teen sum:
def no_teen_sum(a, b, c):
  def fix_teen(n):
    return 0 if n in range(13,15) or n in range(17,20) else n
  return fix_teen(a)+fix_teen(b)+fix_teen(c);
---------------------------------------------------
5.Round sum:
def round_sum(a, b, c):
  return round10(a)+round10(b)+round10(c);
  
def round10(num):
  remain = num%10
  if remain < 5:
    return (num-remain)
  else:
    return ((10-remain)+num)
---------------------------------------------------
6.Close far:
def close_far(a, b, c):
  if abs(b-a) <= 1 and abs(c-a)>1 and abs(c-b) >1:
    return True
  elif abs(c-a) <= 1 and abs(b-a)>1 and abs(b-c) >1:
    return True
  else:
    return False;
---------------------------------------------------
7.Make chocolate
def make_chocolate(small, big, goal):
  re = goal- (big*5)
  biggie = goal%5
  if re < 0:
    if biggie <= small:
      return biggie
    else:
      return -1
  elif re >= 0:
    if re <= small:
      return re
    else:
      return -1;

