class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.is_end = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.is_end

            char = word[i]
            if char in node.children:
                if dfs(i+1, node.children[char]):
                    return True
            elif char == '.':
                for child in node.children:
                    if dfs(i+1, node.children[child]):
                        return True
            return False

        return dfs(0, self.root)
        
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False