class MyHashMap:

    def __init__(self):
        self.data = [-1]

    def put(self, key: int, value: int) -> None:
        if key >= len(self.data):
            self.data += [-1] * (key - len(self.data) + 1)
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key] if key < len(self.data) else -1

    def remove(self, key: int) -> None:
        if key < len(self.data):
            self.data[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)