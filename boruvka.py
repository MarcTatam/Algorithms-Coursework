import numpy as np

def same_tree(forest, node1, node2):
    for tree in forest:
        if node1 in tree and node2 in tree:
            return True
    return False

def get_tree_index(forest, node):
    for tree_index in len(forest):
        if node in forest[tree_index]:
            return tree_index

def boruvka(transition_matrix: np.ndarray):
    dimensions = transition_matrix.shape[0]
    subtrees = []
    minimum_spanning_matrix = np.ones((dimensions,dimensions)) *-1
    incomplete = True
    #Add all nodes to subtree list to get inital config
    for i in range(0,dimensions):
        subtrees.append([i])
    #Main algorithm loop
    while incomplete:
        new_subtrees=subtrees
        completed_nodes = []
        for tree in subtrees:
            lowest_path = ()
            lowest_value = -1
            for node in tree:
                for connection in range(0, dimensions):
                    if node == connection:
                        pass
                    if transition_matrix[node][connection] < lowest_value or lowest_value < 0:
                        if not same_tree(new_subtrees,node,connection):
                            lowest_value = transition_matrix[node][connection]
                            lowest_path  = (node, connection)
            tree1_index = get_tree_index(new_subtrees, lowest_path[0])
            tree2_index = get_tree_index(new_subtrees, lowest_path[1])
            if tree1_index > tree2_index:
                new_tree = new_subtrees[tree2_index] + new_subtrees[tree1_index]
                new_subtrees.pop(tree2_index)
                new_subtrees.pop(tree1_index)
            else:
                new_tree = new_subtrees[tree2_index] + new_subtrees[tree1_index]
                new_subtrees.pop(tree1_index)
                new_subtrees.pop(tree2_index)
        subtrees = new_subtrees
        if len(subtrees) == 1:
            incomplete = false

    print(minimum_spanning_matrix)


if __name__ == "__main__":
    np.ndarray((2,2))
    boruvka(np.ndarray([1,2],[2,1]))