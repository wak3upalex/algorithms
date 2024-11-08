from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# tree creation
root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)
node_c.add_child(node_f)


# DFS (Depth-First Search)
def dfs(node):
    print(node.value)
    for child in node.children:
        dfs(child)


dfs(root)


def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        for child in node.children:
            queue.append(child)


bfs(root)
