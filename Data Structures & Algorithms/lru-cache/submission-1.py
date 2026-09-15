class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUCache = {}

        self.head = self.tail = None

    def remove(self, node):
        # if one node
        if self.head == self.tail == node:
            self.head = self.tail = None
            return
        
        # if removed node is head
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            return
        
        # if removed node is tail
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        # remove in b/w node
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
        return


    def insert(self, node):
        if not self.head and not self.tail:
            self.head = self.tail = node
        # add new node to end of list
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

        return 

    def move(self, node):
        # remove from its position
        self.remove(node)

        # insert at end
        self.insert(node)
        return

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            # move key to end of list & remove from its position
            self.move(self.LRUCache[key])
            return self.LRUCache[key].val
        return -1
       

    def put(self, key: int, value: int) -> None:
        # if key already exists then update its value and move it to end of list
        if key in self.LRUCache:
            self.LRUCache[key].val = value
            self.move(self.LRUCache[key])
            return
        
        # check capacity
        if len(self.LRUCache) == self.capacity:
            # remove least recently used
            rem = self.head
            del self.LRUCache[rem.key]
            self.remove(rem)

        # create node of this value
        newNode = Node(key, value)
        self.LRUCache[key] = newNode
        #insert node
        self.insert(newNode)

        return
        
