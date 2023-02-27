import functools
import heapq

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
print(heapq.nsmallest(3, heap))
# [1, 2, 3]

heap = []
push = functools.partial(heapq.heappush, heap)
smallest = functools.partial(heapq.nsmallest, iterable=heap)

push(1)
push(3)
push(5)
push(2)
push(4)
print(smallest(2))
# [1, 2, 3]
