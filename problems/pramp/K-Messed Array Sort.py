import heapq

def sort_k_messed_array(arr, k):
  pqueue = arr[:k+1]
  heapq.heapify(pqueue)
  
  target_index = 0
  for i in range(k + 1, len(arr)):
    arr[target_index] = heapq.heappop(pqueue)
    heapq.heappush(pqueue, arr[i])
    target_index += 1
    
  while pqueue:
    arr[target_index] = heapq.heappop(pqueue)
    target_index += 1
    
  return arr