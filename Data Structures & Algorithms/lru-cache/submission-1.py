class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # {key: node}
        self.cap = capacity
        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev = self.right.prev
        node.prev, node.next = prev, self.right
        prev.next = self.right.prev = node

    def remove(self, node):
        nxt, prev = node.next, node.prev
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # remove the node and place to the right of list 
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # if key in cache, remove it first
        if key in self.cache:
            self.remove(self.cache[key])

        # update cache
        self.cache[key] = Node(key, value)

        # insert node to the right of the list 
        self.insert(self.cache[key])

        # remove left most node if len(cache) > capacity
        if len(self.cache) > self.cap:
            leastFreq = self.left.next
            self.remove(leastFreq)
            del self.cache[leastFreq.key]

