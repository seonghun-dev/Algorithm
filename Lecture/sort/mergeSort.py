def mergeSort(x):
  if len(x) <= 1:
    return x
  mid = len(x) //2
  leftX = x[:mid]
  rightX = x[mid:]
  leftX = mergeSort(leftX)
  rightx = mergeSort(rightX)
  return merge(leftX,rightX)

def merge(a,b):
  c=[]
  while len(a) > 0 and len(b) > 0:
    if a[0]< b[0]:
      c.append(a.pop(0))
    else:
      c.append(b.pop(0))
  if len(a) == 0:
    c.extend(b)
  else:
    c.extend(a)
  return c

x = [5,2,4,7,1,2,3,6]
print(mergeSort(x))