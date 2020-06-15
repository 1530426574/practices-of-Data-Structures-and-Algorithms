from pprint import pprint

class Trie:

    def __init__(self):
        self.trie = {}

#apply ,apple
    def insert(self, word):
        """
        关键在哪呢？？？t = t[w]
        :param word:
        :return:
        """
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            # print(self.trie) 凑dict
            t = t[w]
        t['#'] = '#'

#apply
    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

#app
    def startsWith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True


trie = Trie()
# trie.insert(['w','o','r','d'])
trie.insert('apply')
pprint(trie.trie)
trie.insert('apple')
pprint(trie.trie)
print(trie.search('apply'))

trie.insert('banana')
pprint(trie.trie)