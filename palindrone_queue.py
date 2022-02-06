class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
        self.size+=1

    def dequeue(self):
        if self.size > 0:
          self.size -=1 
        else:
          self.size =  0 
        return self.items.pop()
    
    def __str__(self):
      ''' Illegal printing method for debugging'''
      out = '\n'
      for i,v  in enumerate(self.items):
        out += f"Q-pos: {self.size- i}".ljust(12) + f"value:{v}".ljust(12) +f"mem-pos: {str(id(i))[-4:]}\n".rjust(12)
      return out

class Deque: #double ended queue
    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)
        self.size +=1

    def addRear(self, item):
        self.items.insert(0,item)
        self.size +=1

    def removeFront(self):
        self.size -=1
        return self.items.pop()

    def removeRear(self):
        self.size -=1
        return self.items.pop(0)

    def sizeof(self):
        if self.size <0:
          self.size = 0 
        return self.size

    def __str__(self):
      out = ''
      for i in self.items:
        out += str(i) +" "
      return out
    
    def debug(self):
      ''' Illegal printing method for debugging'''
      out = '\n'
      for i,v  in enumerate(self.items):
        out += f"Q-pos: {self.size- i}".ljust(12) + f"value:{v}".ljust(12) +f"mem-pos: {str(id(i))[-4:]}\n".rjust(12)
      return out

#make an instance of the queue
q = Queue()
#load into the queue 10 values with values good for debugging
n = 10
[q.enqueue(i) for i in range(1,n+1)] #COMPREHENSION is the same as a for loop
# for i in range(1,n+1):
#   q.enqueue(i)
print(q)
print(str(id(q)))
val = q.dequeue()
print(q)

print("+________________+")
#DEQUE tests
d = Deque()

print(d.isEmpty())
d.addRear(4)
print(d)
d.addRear('dog')
print(d)
d.addFront('cat')
print(d)
d.addFront(True)
print(d)

print(d.sizeof())
d.isEmpty()
print(d)
d.addRear(8.4)
print(d)
d.removeRear()
print(d)
d.removeFront()
print(d)

def pal_checker(a_string):
    char_deque = Deque()
    bad_chars = [" ",",","!",":"]
    for bad_char in bad_chars:
      a_string = a_string.replace(bad_char,"") #remove white spaces
    a_string = a_string.lower()        

    for ch in a_string:
        char_deque.addRear(ch)

    while char_deque.sizeof() > 1:
        first = char_deque.removeFront()
        last = char_deque.removeRear()
        if first != last:
            return False
    return True

words = ["Go hang a salami, im a lasagna hog!",
"radar",
"Slow speed: deep owls",
"A man, a plan, a kind of man-made river, planned",
"Hobos! So!"]
for word in words:
  check = pal_checker(word)
  if check:
    print(f"\"{word}\" is  a palindrone")
  else:
    print(f"\"{word}\" is NOT a palindrone")


