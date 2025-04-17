from graphviz import Digraph

dot = Digraph()

# Add nodes
dot.node('A', 'Root')
dot.node('B', 'Child 1')
dot.node('C', 'Child 2')

# Add edges
dot.edge('A', 'B')
dot.edge('A', 'C')

dot.render('tree', view=True)  # Creates a tree.pdf file and opens it
