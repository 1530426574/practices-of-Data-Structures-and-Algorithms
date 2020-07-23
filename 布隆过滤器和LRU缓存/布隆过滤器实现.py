import mmh3
from bitarry import bitarry

BIT_SIZE = 5 * 1000000


class BloomFilter:

    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarry(size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % seed
            self.bit_array[result] = 1

    def lookup(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed)
            if self.bit_array[result] == 0:
                return 'Nope'
        return 'Probably'
