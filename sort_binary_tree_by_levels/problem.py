from collections import deque


def tree_by_levels(node):
    if node is None:
        return []

    queue = deque([node])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return result
