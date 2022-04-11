def binarySearch(sorted_list, query):
  min_idx, max_idx = 0, len(sorted_list)-1
  while True:
      mid_idx =(min_idx + max_idx)//2
      if query > sorted_list[mid_idx]:
        min_idx = mid_idx
      elif query < sorted_list[mid_idx]:
        max_idx = min_idx
      else:
        query_idx = sorted_list.index(sorted_list[mid_idx])
        break
  return query_idx

x = [2*k -1 for k in range(1,17)]
query_idx = binarySearch(x,27)
print(x)
print("query: ",x[query_idx],"location: ", query_idx)