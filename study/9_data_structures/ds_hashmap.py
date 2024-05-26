class HashMap:
    def __init__(self, size):
        self.hashmap = [None for i in range(size)] # When creating a HashMap a size must be given, for each record the value will be None

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {v[0]}, {v[1]}\n"
            else:
                final += f" - {i}: None\n"
        return final
    
    def key_to_index(self, key):
        count = 0
        for char in key:
            count += ord(char)
        return count % len(self.hashmap)
    
    def insert(self, key, value):
        index_from_key = self.key_to_index(key)
        new_tuple = (key, value)
        self.hashmap[index_from_key] = new_tuple

    # def get(self, key)

# How do we initialize or test this?

hm = HashMap(7)
hm.insert('kay','meulders')
hm.insert('johnny','cage')
hm.insert('frank','sinatra')
hm.insert('duke','nukem')

print(hm)
