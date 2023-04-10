class BinarySearchTree():
    def __init__(self,data):
        self.key=data
        self.lchild=None
        self.rchild=None

    def insert(self,data):           #insert method
        if self.key == None:
            self.key=data
            return
        if self.key==data:                # to avoid insert duplicate elements
            return 
        if self.key>data:
            if self.lchild == None:
                self.lchild=BinarySearchTree(data)
            else:
                self.lchild.insert(data)
        else:
            if self.rchild==None:
                 self.rchild=BinarySearchTree(data)
            else:
                self.rchild.insert(data)

    def search(self,data):                       #search method
        if self.key==data:
            print("data is present")
            return
        if self.key > data:
            if self.lchild==None:
                print("data is not present in the tree")
            else:
                self.lchild.search(data)
        else:
            if self.rchild== None:
                print("data is not present in the tree")
            else:
                self.rchild.search(data)

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")

root=BinarySearchTree(None)
root.insert(10)
root.insert(20)
root.insert(5)
root.insert(30)
root.insert(1)
root.search(1)
root.search(50)
root.preorder()
print()
root.inorder()
print()
root.postorder()