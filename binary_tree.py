class Tree:
    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)
            


if __name__ == "__main__":
    
    root = Tree(15)
    root.left = Tree(12)
    root.right = Tree(18)
    root.left.left = Tree(9)
    root.left.right = Tree(13)
    root.right.left = Tree(17)
    root.right.right = Tree(20)
    preorder(root)
    inorder(root)
    postorder(root)