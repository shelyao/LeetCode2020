class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.end_of_word = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.child:
                root.child[char] = TrieNode()
            root = root.child[char]
        root.end_of_word = True
            
        
    def search(self, word: str) -> bool:
        return self.prefix(word, self.root, 0)
    
    def prefix(self, word, root, start):
        if start == len(word):
            return root.end_of_word
        if word[start] == ".":
            for key in root.child: 
                if self.prefix(word, root.child[key], start + 1): 
                        return True
        elif word[start] in root.child: 
            return self.prefix(word, root.child[word[start]], start + 1)
        else: return False
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)