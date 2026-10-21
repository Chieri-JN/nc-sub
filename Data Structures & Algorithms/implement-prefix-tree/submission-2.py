class PrefixNode: 
    def __init__(self) -> None:
        self.children = {}
        self.prefixes = set()
        self.isEnd = False


class PrefixTree:

    def __init__(self):
        self.node = PrefixNode()

    def insert(self, word: str) -> None:
        node = self.node
        # pref = ""
        n = len(word)
        for i, c in enumerate(word):
            TreeNode = node.children.get(c, PrefixNode())
            # TreeNode.prefixes.add(pref) 
            node.children[c] = TreeNode
            # pref = pref + c
            node = TreeNode
            if i == n - 1:
                node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.node
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.node
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return True
        