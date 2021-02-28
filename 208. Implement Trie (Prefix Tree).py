class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.is_word = False
        self.word = None
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for char in word:
            if char not in root.child:
                root.child[char] = TrieNode()
            root = root.child[char]
                
        root.is_word = True
        root.word = word
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for char in word:
            if char not in root.child: return False
            root = root.child[char]
        return root.is_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for char in prefix:
            if char not in root.child: return False
            root = root.child[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)