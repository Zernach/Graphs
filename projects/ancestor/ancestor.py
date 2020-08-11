from collections import deque

def earliest_ancestor(ancestors, starting_node):

    # Build out a dictionary of child/parent relationships from ancestors.
    # Instantiate a dict —— { key: [list_of_keys_parents] }
    ref = {}
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]

        # If child is not in dict, create it.
        if child not in ref:
            ref[child] = []
        # Add to child's list of parent(s) in the dict.
        ref[child].append(parent)

    # Instantiate a queue, add the starting node to queue.
    q = deque()
    q.append([starting_node])

    # The longest_node will ne returned at the end of the function. 
    # Update the values of longest_node for deepest, furthest ancestor(s).
    # If the input individual has no parents, the function should return -1.
    longest_node = [1,-1]

    # While the queue is not empty
    while len(q) > 0:
        
        # Save first path from queue, and save last_node.
        curr_path = q.popleft()
        last_node = curr_path[-1]

        # If the last node is not in the dict (has no parents)...
        if last_node not in ref:
            # If the length of the current path is longer than the
            # longest previous path, that will be the new longest path
            # and store the node that corresponds with it
            if len(curr_path) > longest_node[0]:
                longest_node = [len(curr_path), last_node]
            if len(curr_path) == longest_node[0] and last_node < longest_node[1]:
                longest_node = (len(curr_path), last_node)

        # If the last node is in the dict (has parents)...
        # Add each parent of last_node to queue.
        else:
            for parent in ref[last_node]:
                q.append(curr_path + [parent])

    return longest_node[1]