def exchange(x, i, j):
  x[i], x[j] = x[j], x[i]
def selectionSort(x):
  n=len(x)
  for i in range(n-1):
    idx = x.index(min(x[i:]))
    exchange(x, i, idx)
    print('exchange',x)
x = [5,2,4,7,1,2,3,6]
print(selectionSort(x))