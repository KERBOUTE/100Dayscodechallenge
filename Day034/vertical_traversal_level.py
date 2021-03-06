from collections import deque, defaultdict as dd
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def print_bottom(root):

    if root == None:
        return

    queue = deque()
    Treemap = dd(list)
    hd = 0
    queue.append((hd, root))
    while queue:

        curr = queue.popleft()

        hd = curr[0]

        Treemap[hd].append(curr[1].data)

        if curr[1].left:
            queue.append((hd - 1, curr[1].left))

        if curr[1].right:
            queue.append((hd + 1, curr[1].right))

    ans = []
    keys = sorted(Treemap.keys())
    for i in keys:
        ans.extend(Treemap[i])
    print(ans)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)
    print_bottom(root)
