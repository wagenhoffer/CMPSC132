class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
    def __str__(self):
      st = ""
      for i in self.items:
        st += hex(id(i))[-3:] + " "
      return st



q = Queue() 
for i in range(1,11):
  print(f"{i} is joining the queue!")
  q.enqueue(i)

for n in range(5):
  # print(f"{q.dequeue()} has left the queue")
  q.dequeue()
  print(q)


print(q.items[::-1])

def hot(q,num):
  for i in range(num):
    out = q.dequeue()
    q.enqueue(out)
  print(f"{q.dequeue()} is a loser!")

hot(q, 22)

# from collections import deque
# dq = deque()
# dq.en
# print(q) :D
# print(hex(id(q)))

# x = [1,2,3,4]
# y = x.copy()
# print(id(x),id(y))
# y*=2
# print(x,y)
