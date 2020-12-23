class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


with open("input.txt") as fp:
    cups = [int(i) for i in fp.read().strip()]


nodes = {}

last_node = None
for i in cups:
    node = Node(i)
    nodes[i] = node
    if last_node is not None:
        last_node.right = node
        node.left = last_node
    last_node = node

# Complete 1 million nodes
for i in range(len(cups)+1, 1_000_001):
    node = Node(i)
    nodes[i] = node
    if last_node is not None:
        last_node.right = node
        node.left = last_node
    last_node = node

# Complete the circle
ptr = nodes[cups[0]]
last_node.right = ptr
ptr.left = last_node

assert len(nodes) == 1_000_000

ptr = nodes[cups[0]]
for i in range(10_000_000):
    if i % 500_000 == 0:
        print(i)
    p_val = ptr.val

    c1 = ptr.right
    c2 = c1.right
    c3 = c2.right

    ptr.right = c3.right
    ptr.right.left = ptr

    d_val = p_val - 1 or 1_000_000
    while d_val in (c1.val, c2.val, c3.val):
        d_val = d_val - 1 or 1_000_000

    d_node = nodes[d_val]

    c3.right = d_node.right
    c3.right.left = c3
    d_node.right = c1
    c1.left = d_node

    ptr = ptr.right

while ptr.val != 1:
    ptr = ptr.right

print(ptr.right.val * ptr.right.right.val)
