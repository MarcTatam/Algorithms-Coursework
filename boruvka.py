import numpy as np

def same_tree(forest : [[int]], node1: int, node2 : int):
    """Checks if two nodes are in the same subtree
    
    Args
    forest - to check for subtree participation
    node1 - first node to check if its in the same subtree
    node2 - second node to check if its in the same subtree

    Returns
    True if they are in the same subtree, false otherwise
    """
    for tree in forest:
        if node1 in tree and node2 in tree:
            return True
    return False

def get_tree_index(forest : [[int]], node : int):
    """Gets the index of a subtree that a node belongs to in a forest
    
    Args
    forest - the forest to find the tree in
    node - the node that we want to find the subtree of
    
    Returns
    Integer representing the subtree index"""
    for tree_index in range(0,len(forest)):
        if node in forest[tree_index]:
            return tree_index

def boruvka(transition_matrix: np.ndarray):
    """Find the minimum spanning tree using boruvkas algorithm. This implmentation assumes that there will be no edges with negative weights and transitions with a weight of -1 are unconnected nodes.

    Args
    transition_matrix - transition matrix of the graph that we are trying to find the MST for

    Returns
    transition matrix for the minimum spanning tree
    """
    dimensions = transition_matrix.shape[0]
    print(transition_matrix)
    subtrees = []
    minimum_spanning_matrix = np.ones((dimensions,dimensions)) *-1
    incomplete = True
    #Add all nodes to subtree list to get inital configuration
    for i in range(0,dimensions):
        subtrees.append([i])
    #Main algorithm loop
    while incomplete:
        new_subtrees=subtrees
        completed_nodes = []
        #For each subtree
        for tree in subtrees:
            lowest_path = ()
            lowest_value = -1
            #Find shortest edge
            for node in tree:
                for connection in range(0, dimensions):
                    if node == connection or transition_matrix[node][connection] == -1:
                        pass
                    elif transition_matrix[node][connection] < lowest_value or lowest_value < 0:
                        if not same_tree(new_subtrees,node,connection):
                            lowest_value = transition_matrix[node][connection]
                            lowest_path  = (node, connection)
            #Join trees
            tree1_index = get_tree_index(new_subtrees, lowest_path[0])
            tree2_index = get_tree_index(new_subtrees, lowest_path[1])
            if tree1_index > tree2_index:
                new_tree = new_subtrees[tree2_index] + new_subtrees[tree1_index]
                new_subtrees.pop(tree1_index)
                new_subtrees.pop(tree2_index)
                new_subtrees.append(new_tree)
            else:
                new_tree = new_subtrees[tree2_index] + new_subtrees[tree1_index]
                new_subtrees.pop(tree2_index)
                new_subtrees.pop(tree1_index)
                new_subtrees.append(new_tree)
            #Add edge to output transition matrix
            minimum_spanning_matrix[lowest_path[0]][lowest_path[1]] = lowest_value
            minimum_spanning_matrix[lowest_path[1]][lowest_path[0]] = lowest_value
        #Check if the algorithm has completed
        subtrees = new_subtrees
        if len(subtrees) == 1:
            incomplete = False
    return minimum_spanning_matrix


if __name__ == "__main__":
    test = np.array([[-1,3,-1,1,-1,-1],
            [3,-1,2,4,2,2],
            [-1,2,-1,-1,1,-1],
            [1,4,-1,-1,-1,-1],
            [-1,2,1,-1,-1,1],
            [-1,2,-1,-1,1,-1]])
    print(boruvka(test))