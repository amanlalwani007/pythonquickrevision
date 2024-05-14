import heapq
li=[5,7,9,1,3]

# be default it implements min heap
heapq.heapify(li)
print("The  created heap is :", end="")
print(list(li))

heapq.heappush(li,4)

print(f"The modified heap after  push is ", end="")
print(list(li))

print(f"the popped and the smallest element  is ", end ="")
print(heapq.heappop(li))

print(f"The  popped item  using heappushpop is ", end ="")
print(heapq.heappushpop(li, 2))

print("the popped item using heapreplace is  :", end="")
print(heapq.heapreplace(li,2))
