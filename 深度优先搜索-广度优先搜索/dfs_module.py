visited = set()


def dfs(node, visited):
    # terminator
    if node in visited:
        return
        visited.add(node)
    # process currrent node level
    # dril down
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited)


def def1(self, root):
    if not root:
        return []

    visited, stack = [], [root]
    while stack:
        node = stack.pop()
        visited.add(node)

        process(node)
        nodes = generated_related_nodes(node)
        stack.add(nodes)


def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop(0)
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
