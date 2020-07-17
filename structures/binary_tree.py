class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.acum = ["1"]

    def insert(self, data):
        if self.data:
            if data > self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data < self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printtree(self):

        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()
            # print(self.data)

    """
    inorder traverse algo
    Traverse the left subtree, i.e., call Inorder(left - subtree)
    Visit the root.
    Traverse the right subtree, i.e., call Inorder(right - subtree)
    """

    def inorder_traverse(self, root):
        if root is None:
            return
        self.inorder_traverse(root.right)
        print(root.data)
        self.inorder_traverse(root.left)

    """
      preorder traverse algo
      Traverse the right subtree
      Visit the root.
      Traverse the lrft subtree
      """

    def preorder_traverse(self, root):
        if root is None:
            yield

        self.preorder_traverse(root.left)
        print(root.data)
        self.preorder_traverse(root.right)

    def tree_to_list_inorder(self, root):
        if root is None:
            return []

        left_list = self.tree_to_list_inorder(root.left)
        right_list = self.tree_to_list_inorder(root.right)
        return left_list + [root.data] + right_list



