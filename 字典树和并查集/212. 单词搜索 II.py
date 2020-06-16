class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = '#'

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords

#
# class TrieNode():
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.isWord = False
#
#
# class Trie():
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         node = self.root
#         for w in word:
#             node = node.children[w]
#         node.isWord = True
#
#     def search(self, word):
#         node = self.root
#         for w in word:
#             node = node.children.get(w)
#             if not node:
#                 return False
#         return node.isWord

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
        t['#'] = word
        return self.trie

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

class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        d = trie.trie
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, d, i, j, "", res)
        return res


    def dfs(self, board, d:dict, i, j, path, res):
        if d.get('#'):
            res.append(path)
            d['#'] = {}
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        d = d.get(tmp)
        if not d:
            return
        board[i][j] = "visited"
        self.dfs(board, d, i + 1, j, path + tmp, res)
        self.dfs(board, d, i - 1, j, path + tmp, res)
        self.dfs(board, d, i, j - 1, path + tmp, res)
        self.dfs(board, d, i, j + 1, path + tmp, res)
        board[i][j] = tmp