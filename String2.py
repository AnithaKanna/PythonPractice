1.Double Char
def double_char(str):
  newstr = ''
  for i in range(len(str)):
    newstr += str[i]+str[i]
  return newstr;
-------------------------------------------
2.Count hi
def count_hi(str):
  num = 0
  for i in range(len(str)-1):
    if str[i] == 'h' and str[i+1] == 'i':
      num += 1
  return num
-------------------------------------------
3.CAT DOG
def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)-2):
    if str[i] == 'c' and str[i+1] == 'a' and str[i+2] == 't':
      cat += 1
    elif str[i:i+3] == 'dog':
      dog += 1
  return True if cat == dog else False
-------------------------------------------
4.Count code:
def count_code(str):
  sum = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      sum += 1
  return sum
-------------------------------------------
5.End other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a) >= len(b):
    l = len(b)
    if a[-l:] == b:
      return True
    else:
      return False
  else:
    l = len(a)
    if b[-l:] == a:
      return True
    else:
      return False
  
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (a.endswith(b) or b.endswith(a) )
-------------------------------------------
6.Xyz there:
def xyz_there(str):
  for i in range(len(str)-2):
    if str[i:i+3] == 'xyz' and str[i-1] != '.':
      return True
  return False


