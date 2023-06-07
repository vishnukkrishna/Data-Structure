# Prifix Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        self._delete_helper(self.root, word, 0)

    def _delete_helper(self, node, word, index):
        if index == len(word):
            node.is_end_of_word = False
            return len(node.children) == 0

        char = word[index]
        if char not in node.children:
            return False

        should_delete_node = self._delete_helper(node.children[char], word, index + 1)

        if should_delete_node:
            del node.children[char]
            return len(node.children) == 0

        return False


tr = Trie()
tr.insert("vishnu")
tr.insert("her")
tr.delete("her")
print(tr.search("vishnu"))