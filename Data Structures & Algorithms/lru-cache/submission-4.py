"""

"""
class DLL:
    def __init__(self, value, key):
        self.key = key
        self.val = value 
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.cap = capacity
        self.head = None
        self.end = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.reorder(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print(f"putting Key: {key} val: {value}")
        if key in self.cache:
            node = self.cache[key]
            node.val =  value
            self.reorder(node)
        # incr size
        else:
            if self.size >= self.cap:
                self.evict()
                self.size -= 1
            node = DLL(value, key)
            node.nxt = self.head
            if self.head:
                self.head.prev = node

            self.head = node
            if not self.end:
                self.end = node
            self.size += 1
            self.cache[key] = node

    def reorder(self, node: DLL):
        if node != self.head:
            nxt = node.nxt
            prv = node.prev
            if nxt:
                nxt.prev = prv
            if prv:
                prv.nxt = nxt
            if self.end == node:
                self.end = prv if prv else node
            node.nxt = self.head
            self.head.prev = node
            self.head = node

    def evict(self):
        tp = self.end
        self.end = tp.prev
        if self.end:
            self.end.nxt = None
        tp.prev = None
        self.cache.pop(tp.key)
