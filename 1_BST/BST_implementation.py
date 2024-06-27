class BST:

    def __init__(self,data):

        self.data = data
        self.l_child = None
        self.r_child = None

    def insert(self,data):

        if self.data is None:
            self.data = data
            return
        if self.data == data:
            return
        if self.data > data:
            if self.l_child:
                self.l_child.insert(data)
            else:
                self.l_child = BST(data)
        else:
            if self.r_child:
                self.r_child.insert(data)
            else:
                self.r_child = BST(data)

    def search(self,node):

        if self.data == node:
            print("Node is Found...")
            return
        if self.data > node:
            if self.l_child:
                self.l_child.search(node)
            else:
                print("Node was Not Found...")
        else:
            if self.r_child:
                self.r_child.search(node)
            else:
                print("Node was Not Found")
    def pre_order(self):

        print(self.data,end=" ")

        if self.l_child:
            self.l_child.pre_order()
        if self.r_child:
            self.r_child.pre_order()

    def in_order(self):

        if self.l_child:
            self.l_child.in_order()

        print(self.data, end=" ")

        if self.r_child:
            self.r_child.in_order()

    def post_order(self):

        if self.l_child:
            self.l_child.in_order()
        if self.r_child:
            self.r_child.in_order()

        print(self.data, end=" ")


root = BST(21)
l = [34,2,54,98,22,11,52,68,46,26]
for i in l:
    root.insert(i)

#root.search(7)
#root.pre_order()
#root.post_order()
root.in_order()
