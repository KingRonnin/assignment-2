import hashlib

def simple_hash(key):
    key_str = str(key)
    ascii_sum = sum(ord(char) for char in key_str)
    return ascii_sum

def salted_hash(key, salt):
    combined = f"{key}{salt}".encode('utf-8')
    hash_value = hashlib.sha256(combined).hexdigest()
    return hash_value[:8]
