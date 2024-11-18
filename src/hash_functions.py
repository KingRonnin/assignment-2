import hashlib
import os

def simple_hash(key): # Takes in a key
    key_str = str(key) # Convert key to string
    ascii_sum = sum(ord(char) for char in key_str) # calculates the sum of the ascii values of char
    return ascii_sum % 10 # return value between 0 and 9 by getting the remainder of ascii_sum divided by 10

"""
Generates a salted hash from a given key.

This function converts the key to a string, computes the sum of the ASCII values of its characters,
generates a random salt based on that sum, and then creates a SHA-256 hash of the combined key and salt.
It returns the first eight characters of the hexadecimal representation of the hash.

Args:
    key: The input key to be hashed.

Returns:
    A string representing the first eight characters of the salted hash.
"""
def salted_hash(key):
    key_str = str(key)
    ascii_sum = sum(ord(char) for char in key_str)
    salt = os.urandom(ascii_sum)
    combined = f"{key}{salt}".encode('utf-8')
    hash_value = hashlib.sha256(combined).hexdigest() # returns the hash value into a hexidecimal string
    return hash_value[:8]
