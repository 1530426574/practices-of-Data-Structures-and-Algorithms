from collections import defaultdict,deque
from pprint import pprint

#关键在于用一个path存储遍历得到的节点，直到满足条件。
## Solution 1
def findLadders(self, beginWord, endWord, wordList):
	if not endWord or not beginWord or not wordList or endWord not in wordList \
		or beginWord == endWord:
		return []

	L = len(beginWord)

	# Dictionary to hold combination of words that can be formed,
	# from any given word. By changing one letter at a time.
	all_combo_dict = defaultdict(list)
	for word in wordList:
		for i in range(L):
			all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

	# Shortest path, BFS
	ans = []
	queue = deque()
	queue.append((beginWord, [beginWord]))
	visited = set([beginWord])
	found = False
	while queue and not found:
		# print(queue)
		length = len(queue)
		# print(queue)
		localVisited = set()
		for _ in range(length):
			word, path = queue.popleft()
			for i in range(L):
				for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
					if nextWord == endWord:
						# path.append(endword)
						ans.append(path+[endWord])
						found = True
					if nextWord not in visited:
						localVisited.add(nextWord)
						queue.append((nextWord, path+[nextWord]))
		visited = visited.union(localVisited)
	return ans


class Solution2:
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res
