from anytree import Node, RenderTree

class MyNode(Node):
    def __init__(self, child,parent=None):
        super().__init__(child,parent)
        self.value=0


root = MyNode("Root")
child1 = MyNode("Child1", parent=root)
child2 = MyNode("Child2", parent=root)
grandchild = MyNode("Grandchild", parent=child1)

for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")
