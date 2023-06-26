class HashTable:
    def __init__(self):
        self.size = 10  
        self.table = [[] for _ in range(self.size)]  

    def hash(self, key):
        
        return hash(key) % self.size

    def set(self, key, value):
        
        index = self.hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value  
                return
        self.table[index].append([key, value])  

    def get(self, key):
        
        index = self.hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]  
        return None  

    def has(self, key):
        
        index = self.hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return True
        return False

    def keys(self):
        
        keys = []
        for bucket in self.table:
            for kvp in bucket:
                if kvp[0] not in keys:
                    keys.append(kvp[0])
        return keys
