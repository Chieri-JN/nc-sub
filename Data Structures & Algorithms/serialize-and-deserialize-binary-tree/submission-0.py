# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append(node)
            else:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        # serial = str(res)[1:-1] # remove '[' and ']'
        serial = ""
        for node in res:
            serial = serial + str(node) + ","

        # print(serial[:-1])
        
        return serial[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        cnt = [0]

        deserial = data.split(",")
        n = len(deserial)
        # rootVal = 
        def dfs():
            if cnt[0] >= n or deserial[cnt[0]] == "None":
                cnt[0] += 1
                return
            else:
                val = int(deserial[cnt[0]])
                node = TreeNode(val)
                cnt[0] += 1
                node.left = dfs()
                node.right = dfs()
                return node

        root = dfs()

        return root


