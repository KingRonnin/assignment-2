from hash_functions import simple_hash, salted_hash
from hash_table import HashTable

def main():
    keys = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon', 'pear', 'peach', 'mango', 'plum']
    
    # 1. Simple Hash Function
    print('Simple Hash Function Results: ')
    for key in keys:
        print(f"Key: {key}, Hash: {simple_hash(key)}")
    print()
    
    # 2. Hashtable with Collision Handling
    print("HashTable with Chaining: ")
    hash_table = HashTable()
    for key in keys:
        hash_table.insert(key, len(key))
    
    for key in keys:
        value = hash_table.search(key)
        print(f"Key: {key}, Value: {value}")
    print()
    
    # 3. Salted Hash Function
    print("Salted Hash Function Results: ")
    salt = "12345" # Example
    for key in keys:
        print(f"Key: {key}, Salted Hash: {salted_hash(key, salt)}")
    
if __name__ == "__main__":
    main()