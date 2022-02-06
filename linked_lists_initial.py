"""
The world's worst Docstring for a Linked List - USE A DOCSTRING GENERATOR!
List() creates a new list that is empty. It needs no parameters and returns an empty list.

add(item) adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.

remove(item) removes the item from the list. It needs the item and modifies the list. Raise an error if the item is not present in the list.

search(item) searches for the item in the list. It needs the item and returns a boolean value.

is_empty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.

size() returns the number of items in the list. It needs no parameters and returns an integer.

append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.

index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.

insert(pos, item) adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.

pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.

pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list."""

class Node:
    def __init__(self, data, next=None):
      self.data = data
      self.next = next
        
    def __repr__(self):
      return f'Node({self.data}, {repr(self.next)})'

    def debug(self):
      return f'Node({self.data}, ID:{str(id(self))[-4:]},  {repr(self.next)})'

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

print(node1)
print(node1.debug())

# #LINK THESE ITEMS UP
node1.next = node2
node2.next = node3
print(node1)

class LinkedList:
  def __init__(self, head=None):
      self.head = head
      self._current = None #Current position
      self.theend = Node("THEEND")
      self.head.next = self.theend

  def __repr__(self):
      return f'LinkedList({repr(self.head)})'
  
  def is_empty(self):
    return self.head == None

  def add(self, item): #this is a left add, what about right add?
    temp = Node(item)
    temp.set_next(self.head)
    self.head = temp

  def radd(self,item):
    current = self.head
    while current.next: #would while current: work just as well? 
        current = current.next
    current.next = Node(item)



  def size(self):
    current = self.head
    count = 0
    while current is not None: #would while current: work just as well? 
        count = count + 1
        current = current.next
    return count

  def search(self, item):
    current = self.head
    while current is not None:
        if current.data == item:
            return True
        current = current.next
    return False

  def remove(self, item):
    current = self.head
    previous = None
    while current is not None:
        if current.data == item:
            break
        previous = current
        current = current.next
    if current is None:
        raise ValueError("{} is not in the list".format(item))
    if previous is None:
        self.head = current.next
    else:
        previous.next = current.next

  ###ITERATORS <-- explain this
  def __iter__(self):
      self._current = None
      return self

  def __next__(self):
      """Standard python iterator method"""
      if self.is_empty() or self._current.data == "THEEND": 
          raise StopIteration()
      elif self._current is None:
          self._current = self.head
          return self._current
      self._current = self._current.next
      return self._current



ll = LinkedList(node1)
print(ll)
print("___________________")
for n in ll:
  print(n.data)