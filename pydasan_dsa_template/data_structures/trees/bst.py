from collections import deque

# Node structure
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

def getHeight(root, h):
    if root is None:
        return h - 1
    return max(getHeight(root.left, h + 1), getHeight(root.right, h + 1))

def levelOrder(root):
    queue = deque()
    queue.append((root, 0))

    lastLevel = 0
    height = getHeight(root, 0)
    while queue:
        node, lvl = queue.popleft()

        if lvl > lastLevel:
            print()
            lastLevel = lvl

        # all levels are printed
        if lvl > height:
            break

        # printing null node
        print("N" if node.data == -1 else node.data, end=" ")

        # null node has no children
        if node.data == -1:
            continue

        if node.left is None:
            queue.append((Node(-1), lvl + 1))
        else:
            queue.append((node.left, lvl + 1))

        if node.right is None:
            queue.append((Node(-1), lvl + 1))
        else:
            queue.append((node.right, lvl + 1))

def insert(root, key):
    temp = Node(key)

    # If tree is empty
    if root is None:
        return temp

    # Find the node who is going to have 
    # the new node as its child
    curr = root
    while curr is not None:
        if curr.data > key and curr.left is not None:
            curr = curr.left
        elif curr.data < key and curr.right is not None:
            curr = curr.right
        else:
            break

    # If key is smaller, make it left 
    # child, else right child
    if curr.data > key:
        curr.left = temp
    else:
        curr.right = temp

    return root


if __name__ == "__main__":
    
    root = None
    root = insert(root, 22)
    root = insert(root, 12)
    root = insert(root, 30)
    root = insert(root, 8)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 15)
    
    # print the level order 
    # traversal of the BST
    levelOrder(root)