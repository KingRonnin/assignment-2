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
    
    """
    Inserts a key-value pair into the hash table.

    This method computes the index for the given key using a hashing function and creates a new node for the key-value pair. 
    If the corresponding slot in the hash table is empty, it places the new node there; otherwise, it traverses the linked list to either update the value if the key exists or append the new node.

    Args:
        key: The key to be inserted into the hash table.
        value: The value associated with the key.
    """
    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)
        if not self.table[index]:
            self.table[index] = new_node # Places new node if table is empty
        else:
            current = self.table[index]
            while current.next and current.key != key:
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node
    
    """
    Retrieves the value associated with a given key from the hash table.

    This method computes the index for the specified key using a hashing function and traverses the linked list at that index to find the corresponding value. 
    If the key is found, the associated value is returned; otherwise, None is returned.

    Args:
        key: The key whose associated value is to be retrieved.

    Returns:
        The value associated with the key if found; otherwise, None.
    """
    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None