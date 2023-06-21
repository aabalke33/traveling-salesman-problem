# Class for Hash Table
class HashTable:

    # Adapted from "Webinar - 1 - Let’s Go Hashing", published 12/24/2022
    # Initializes a list of size 40
    def __init__(self, capacity=40):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Adds (inserts) key value pair into Hash Table
    def add(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = value
                return True

        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Gets (Lookups / Searches) for value based on key
    def get(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Deletes (Removes) pair based on key
    def delete(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # Prints all pairs in Hash Table
    def print(self):
        for value in self.table:
            if value is not None:
                print(str(value))
