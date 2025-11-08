from collections import defaultdict, deque

def count_sink_nodes_dfs(graph):
    """
    Count sink nodes using iterative DFS traversal.
    A sink node is identified as a node with no outgoing edges.
    """
    def is_sink_node(node):
        """Check if a node is a sink node using DFS"""
        stack = [node]
        visited = set()
        
        while stack:
            current = stack.pop()
            
            if current not in visited:
                visited.add(current)
                
                if graph[current]:
                    return False
                
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return True
    
    sink_count = 0
    all_nodes = set(graph.keys())
    
    for node in all_nodes:
        if is_sink_node(node):
            sink_count += 1
    
    return sink_count

graph = {
    0: [1, 2],
    1: [3],
    2: [1],
    3: [],
    4: [],
    5: [4]
}

print(f"Sink nodes count: {count_sink_nodes_dfs(graph)}")