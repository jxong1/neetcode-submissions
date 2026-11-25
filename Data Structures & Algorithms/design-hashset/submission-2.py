class MyHashSet:

    def __init__(self):
        self.data = [False]

    def add(self, key: int) -> None:
        if key >= len(self.data):
            self.data += [False] * (key - len(self.data) + 1)
        self.data[key] = True

    def remove(self, key: int) -> None:
        if key < len(self.data):
            self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key] if key < len(self.data) else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)