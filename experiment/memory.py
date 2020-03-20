import queue
import hashlib
from random import randrange


# Various implementations of caching. This file has stub implementations.

class Memory:
    '''Basic lookup'''

    def __init__(self):
        self.hit_count = 0

    def get_hit_count(self):
        return self.hit_count

    def name(self):
        return "Memory"

    def lookup(self, address):
        # This one actually has no cache, so every lookup requires a
        # memory hit.
        self.hit_count += 1
        string = str(address ^ 3).encode()
        return hashlib.md5(string).hexdigest()[:8]


class CyclicCache(Memory):
    '''Cyclic Cache'''

    def __init__(self, size=4):
        super().__init__()
        self.hit_count = 0
        self.cache = {}
        self.max = size

    def name(self):
        return "Cyclic"

    def lookup(self, address):
        if address in self.cache.keys():
            # print("Cyclic Cache Access ", end="")
            return self.cache[address]
        else:
            # print("Memory Access", end=" ")
            # self.hit_count += 1
            # string = str(address ^ 3).encode()
            # value = hashlib.md5(string).hexdigest()[:8]
            value = super().lookup(address)
            if len(self.cache) == self.max:
                replace = list(self.cache)[0]
                del self.cache[replace]
            self.cache[address] = value
            return self.cache[address]


class LRUCache(Memory):
    '''LRU Cache'''

    def __init__(self, size=4):
        super().__init__()
        self.hit_count = 0
        self.cache = {}
        self.max = size

    def name(self):
        return "LRU"

    def lookup(self, address):
        if address in self.cache.keys():
            # print("LRU Cache Access ", end="")
            self.cache[address][1] = 0
            for key in self.cache.keys():
                if key != address:
                    self.cache[key][1] += 1
            return self.cache[address][0]
        else:
            # print("Memory Access", end=" ")
            # self.hit_count += 1
            # string = str(address ^ 3).encode()
            # value = hashlib.md5(string).hexdigest()[:8]
            value = super().lookup(address)
            if len(self.cache) == self.max:
                last_address = list(self.cache.keys())[0]
                maximum = 0
                for key in self.cache.keys():
                    if maximum < self.cache[key][1]:
                        maximum = self.cache[key][1]
                        last_address = key
                del self.cache[last_address]
            for key in self.cache.keys():
                if key != address:
                    self.cache[key][1] += 1
            self.cache[address] = [value, 0]
            return value


class RandomCache(Memory):
    '''Random Cache'''

    def __init__(self, size=4):
        super().__init__()
        self.hit_count = 0
        self.cache = {}
        self.max = size

    def name(self):
        return "Random"

    def lookup(self, address):
        if address in self.cache.keys():
            # print("Cyclic Cache Access ", end="")
            return self.cache[address]
        else:
            # print("Memory Access", end=" ")
            # self.hit_count += 1
            # string = str(address ^ 3).encode()
            # value = hashlib.md5(string).hexdigest()[:8]
            value = super().lookup(address)
            if len(self.cache) == self.max:
                replace = list(self.cache.keys())[randrange(0, self.max)]
                del self.cache[replace]
            self.cache[address] = value
            return self.cache[address]
