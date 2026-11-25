class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.capacity = 0
        self.maxCap = capacity

    def get(self, key: int) -> int:
        ans = -1
        if key in self.cache.keys():
            node = self.cache[key]
            ans = node.val
            nodep = node.prev
            noden = node.next
            nodep.next = noden
            noden.prev = nodep

            tmp = self.tail.prev
            tmp.next = node
            node.prev = tmp
            self.tail.prev = node
            node.next = self.tail
        return ans

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            node = self.cache[key]
            node.val = value
            nodep = node.prev
            noden = node.next
            nodep.next = noden
            noden.prev = nodep

            tmp = self.tail.prev
            tmp.next = node
            node.prev = tmp
            self.tail.prev = node
            node.next = self.tail
            return

        new = Node(key, value)
        self.cache[key] = new

        # Insert to back
        tmp = self.tail.prev
        tmp.next = new
        new.prev = tmp
        new.next = self.tail
        self.tail.prev = new
        self.capacity += 1

        if self.capacity > self.maxCap:
            tmp = self.head.next
            self.head.next = tmp.next
            self.head.next.prev = self.head
            self.capacity -= 1
            del(self.cache[tmp.key])

class Node:

    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None