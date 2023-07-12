# SuffixTrie
class SuffixTrieNode:
    def __init__(self):
        self.children = {}


class SuffixTrie:
    def __init__(self):
        self.root = SuffixTrieNode()

    def insert(self, word):
        for i in range(len(word)):
            self._insert_suffix(word[i:], i)

    def _insert_suffix(self, suffix, index):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTrieNode()
            node = node.children[char]
        node.index = index

    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.index if hasattr(node, "index") else None


trie = SuffixTrie()
word = "banana"
trie.insert(word)
pattern = "ana"
index = trie.search(pattern)
if index is not None:
    print(f"The pattern '{pattern}' is found at index {index}.")
else:
    print(f"The pattern '{pattern}' is not found.")
