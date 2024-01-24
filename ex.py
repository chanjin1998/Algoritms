import sys
import heapq

min_heap = []
max_heap = []
cnt_i = 0
cnt_d = 0
N = int(sys.stdin.readline())
for _ in range(N):
  T = int(sys.stdin.readline())
  cnt_i = 0
  cnt_d = 0
  for _ in range(T):
    cal, num = sys.stdin.readline().split()
    num = int(num)
    if cal == 'I':
      cnt_i += 1
      heapq.heappush(min_heap, num)
      heapq.heappush(max_heap,(-num,num))
    else:
      cnt_d += 1
      if num == 1:
        if len(max_heap) == 0:
          pass
        else:
          
          heapq.heappop(min_heap)
          min_heap.clear()
          for i in max_heap:
            heapq.heappush(min_heap,i[1])
      elif num == -1:
        if len(min_heap) ==0:
          pass
        else:
          heapq.heappop(min_heap)
          min_heap.clear()
          for i in max_heap:
            heapq.heappush(min_heap,i[1])

      if (cnt_i - cnt_d) <= 0:
        min_heap.clear()
        max_heap.clear()
  if (cnt_i - cnt_d) <= 0:
      print('EMPTY')
  else:
      print(heapq.heappop(max_heap)[1],heapq.heappop(min_heap))