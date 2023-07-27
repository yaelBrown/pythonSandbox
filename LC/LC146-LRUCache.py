class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        retrieve = None
        print(self.cache)
        print(f"searching for key: {key}")
        idx = 0
        for i in self.cache:
            if i[0] == key:
                retrieve = i
                del self.cache[idx]
                self.cache = self._insertInFront(self.cache, retrieve)
                print(self.cache)
                print(f"found: {retrieve}\n")
                return retrieve[1]
            idx += 1
        print(f"notFound: {retrieve}\n")
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity: del self.cache[self.capacity - 1]
        self.cache = self._insertInFront(self.cache, [key, value])
    
    def _insertInFront(self, l, v):
        try:
            return [v] + l
        except:
            print(f"insertion of {v} into {l} failed")
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)