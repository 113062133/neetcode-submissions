class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = {}
        self.capacity = capacity

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def insert(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        else:
            node = self.hash_map[key]
            self.remove(node)
            self.insert(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            old_node = self.hash_map[key]
            self.remove(old_node)
        
        new_node = Node(key, value)
        self.hash_map[key] = new_node
        self.insert(new_node)

        if len(self.hash_map) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.hash_map[lru.key]