
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# BFS - Level Order Traversal
def BFS(root):
    if root is None:
        return

    queue = deque([root])

    print("BFS:", end=" ")

    while queue:
        current = queue.popleft()

        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print()


# DFS - Preorder Traversal
def DFS(root):
    if root is None:
        return

    print(root.data, end=" ")

    DFS(root.left)
    DFS(root.right)


# Main Program
def main():

    root = Node("B")

    root.left = Node("A")
    root.right = Node("J")

    root.left.left = Node("E")
    root.left.right = Node("N")

    root.right.left = Node("T")
    root.right.right = Node("I")

    root.left.left.left = Node("N")
    root.left.left.right = Node("G")

    print("================================")
    print(" BINARY TREE - BAJENTING")
    print("================================")

    print("          B")
    print("        /   \\")
    print("       A     J")
    print("      / \\   / \\")
    print("     E   N T   I")
    print("    / \\")
    print("   N   G")

    print("\nTraversal Results:")

    BFS(root)

    print("DFS:", end=" ")
    DFS(root)

    print()


if __name__ == "__main__":
    main()
