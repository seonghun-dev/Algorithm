
def insertSort(x):
  n = len(x)
  for curIdx in range(1,n):
      for i in range(curIdx, 0, -1):
          if x[i] < x [i-1]:
            x[i],x[i-1] = x[i-1], x[i]
            print(curIdx, x)
          else:
            break
x = [5,2,4,6,1,3]

print(insertSort(x))