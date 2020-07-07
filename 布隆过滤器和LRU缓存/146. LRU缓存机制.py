class DLinkNode:

    def __init__(self,key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = next

class LRUCache:

    def __init__(self,capacity: int):
        self.cache = dict()
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self,key: int):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self,key:int, value: int):
        if key not in self.cache:
            node = DLinkNode(key,value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size >self.capacity:
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)


    def move_to_head(self,node: DLinkNode):
        self.remove_node(node)
        self.add_to_head(node)

    def add_to_head(self,node:DLinkNode):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node

    def remove_node(self,node: DLinkNode):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node
