# the third problem is to find the left side nodes in binary tree
from collections import deque
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def insert(root , key ):
    if root is None:
        return Node(key)
    queue = deque([root])
    while queue:
        temp = queue.popleft()
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)

        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)
    return root

def left_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            # First node in this level
            if i == 0:
                result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

def build_tree(arr):
    if not arr or arr[0] == 'N':
        return None

    root = Node(int(arr[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        if arr[i] != 'N':
            node.left = Node(int(arr[i]))
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] != 'N':
            node.right = Node(int(arr[i]))
            queue.append(node.right)
        i += 1

    return root

arr = [1, 2,'N',3, 4, 5, 'N']
root = build_tree(arr)
print(left_view(root))