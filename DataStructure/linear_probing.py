
# Linear Probing
# Hash Table

class HashTable(object):

    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, data):
        index = self.hashFunction(key)

        # if not None .... its a collision

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data # update
                return

            # Rehash try to find another slot
            index = index + 1 % self.size

        # Insert
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):
        index = self.hashFunction(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = index + 1 % self.size

        return None

    def hashFunction(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])
            return sum % self.size

if __name__ == "__main__":

    table = HashTable()

    table.put("orange", 10)
    table.put("apple", 20)
    table.put("banana", 30)
    table.put("strawberry", 40)

    print(table.get("apple"))