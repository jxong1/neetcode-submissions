class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.is_end = True

    def search(self, word: str, start=0, startNode=None) -> bool:
        if not startNode:
            curr = self.root
        else:
            curr = startNode
        for i in range(start, len(word)):
            char = word[i]
            if char == '.':
                for child in curr.children:
                    if self.search(word, i+1, curr.children[child]):
                        return True
                return False
            elif char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.is_end
        
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False