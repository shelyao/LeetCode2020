class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.child = {}
        self.word = ''
class WordDict(object):
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.is_word = True
        node.word = word
        
    def findWord(self, word):
        node = self.root
        for char in word:
            if char not in node.child: return False
            node = node.child[char]
        return True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board: return []
        res = []
        m, n = len(board), len(board[0])
        wordDict = WordDict()
        
        for word in words:
            wordDict.addWord(word)
        
        def search(x, y, node):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == '#': return
            nextNode = node.child.get(board[x][y])
            if nextNode is None: return
            if nextNode.is_word: res.append(nextNode.word)
            temp = board[x][y]
            board[x][y] = '#'
            search(x + 1, y, nextNode)
            search(x - 1, y, nextNode)
            search(x, y + 1, nextNode)
            search(x, y - 1, nextNode)
            board[x][y] = temp
            
        for i in range(m):
            for j in range(n):
                search(i, j, wordDict.root)
        return list(set(res))