from anytree import Node, RenderTree

root = Node("Root")
child1 = Node("Child1", parent=root)
child2 = Node("Child2", parent=root)
grandchild = Node("Grandchild", parent=child1)

for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")
