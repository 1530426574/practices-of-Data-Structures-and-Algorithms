from collections import defaultdict
from pprint import pprint
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        """
        关键在哪呢，广度优先遍历的概念->每层轮询访问。
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        l = len(beginWord) #单词列表的所有单词长度一致
        d = defaultdict(list)
        #wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        for word in wordList:
            for i in range(3):
                key = word[:i] + '*' + word[i + 1:]
                d[key].append(word)

        queue = [(beginWord,1)]
        visited ={beginWord:True}
        while queue:
            cur,level = queue.pop(0)
            for i in range(l):
                key1 = cur[:i]+'*'+cur[i+1:]
                for word in d[key1]:  #key不存在的话，value默认为[]
                    if word == endWord:
                        return level +1
                    if not word  in visited:
                        visited[word]=True
                        queue.append((word,level+1)) #相当于把每一层的节点都放入队列当中。
                d[key1]= []
        return 0
