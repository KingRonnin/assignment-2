class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        key_str = str(key)
        ascii_sum = sum(ord(char) for char in key_str)
        return ascii_sum % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)
        if not self.table[index]:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = new_node
    
    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None