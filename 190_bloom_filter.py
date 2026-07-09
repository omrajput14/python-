import math

class BloomFilter:
    def __init__(self, items_count, fp_prob):
        '''
        items_count : int
            Number of items expected to be stored in bloom filter
        fp_prob : float
            False Positive probability in decimal
        '''
        self.fp_prob = fp_prob
        self.size = self.get_size(items_count, fp_prob)
        self.hash_count = self.get_hash_count(self.size, items_count)
        self.bit_array = [0] * self.size

    def add(self, item):
        '''
        Add an item in the filter
        '''
        for i in range(self.hash_count):
            # A simple deterministic hash function
            digest = hash(f"{i}_{item}") % self.size
            self.bit_array[digest] = 1

    def check(self, item):
        '''
        Check for existence of an item in filter
        '''
        for i in range(self.hash_count):
            digest = hash(f"{i}_{item}") % self.size
            if self.bit_array[digest] == 0:
                return False
        return True

    @classmethod
    def get_size(cls, n, p):
        '''
        Return the size of bit array(m) to used using formula
        '''
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)

    @classmethod
    def get_hash_count(cls, m, n):
        '''
        Return the hash function(k) to be used using formula
        '''
        k = (m/n) * math.log(2)
        return int(k)

if __name__ == '__main__':
    bloomf = BloomFilter(20, 0.05)
    print("Size of bit array:", bloomf.size)
    print("False positive Probability:", bloomf.fp_prob)
    print("Number of hash functions:", bloomf.hash_count)

    words_to_add = ['abound', 'abounds', 'abundance', 'abundant', 'accessible']
    word_absent = ['bluff', 'cheater', 'hate', 'war', 'humanity']

    for word in words_to_add:
        bloomf.add(word)

    for word in words_to_add:
        print(f"'{word}' is present:", bloomf.check(word))

    for word in word_absent:
        print(f"'{word}' is present:", bloomf.check(word))
