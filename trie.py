class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()
