
class HashMap:
    def __init__(self):
        self.size = 30
        self.arr = [None for i in range(self.size)]

    def get_hash(self, key):
        sum_of_char=0
        for char in key:
            sum_of_char+=ord(char)
        return sum_of_char % self.size

    def add(self, key,val):
        index = self.get_hash(key)
        self.arr[index] = val

    def get_items(self, key):
        index = self.get_hash(key)
        return self.arr[index]


test = HashMap()


test.add("march 6",120)
test.add("march 8",140)
test.add("march 9",180)

print(test.arr)







