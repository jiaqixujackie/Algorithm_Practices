
### https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/
 
"""
based on an adjacency matrix (graph) and a starting vertex (v), 
find a hamiltonian_cycle if possible.
    1.  [selection function] find all vertices that are adjacent to v 
    2.  [feasible function] from those adjacent vertices, find the ones 
        that have not yet been visited.
    3.  [objective function] implement backtracing to build the 
        hamiltonian path. We need to use the feasible function to extend 
        the hamiltonian path. 
    4.  [solution function] this is for the user. the user need to give 
        us a graph and a starting vertex, so that we can try to find the
        hamiltonian cycle for them.
"""





def next_vertices(graph, v):  # [selection function]
    """
    input:  a graph (adjacency matrix) and a vertex (v)
    output: a list which store all the vertices that are 
            adjacent (directly connected) to v
    """
    return [i for i in range(len(graph)) if graph[v][i]] 


def feasible_vertices(graph,v,visited): # [feasible function]
    """
    input:  a graph, a vertex, and a list (visited) of sublist
            [[0,T/F], [1,T/F], ...]. each sublist contains an index
            and a boolean value, T if visited, F if not yet visited.
    output: a list of vertices that are adjacent to v and has not
            been visited yet. 
    """
    # step 1: find all vertices that are adjacent to v
    next_v = next_vertices(graph,v)

    # step 2: from the adjacent vertices, find ones that can be visited.
    feasible_v = []
    for candidate in next_v:
        if visited[candidate][1] == False: # condition: not yet been visited
            feasible_v.append(candidate)
    
    # step 3: returns the result
    return feasible_v


def backtracking(graph,entry,v,visited,path): # [objective function]
    """
    entry, v  ==  the starting vertex and the current vertex
    the graph == help to identify adjacent vertices
    visited ==  is required to filter out the set of feasible 
                adjacent vertices
    path == to form the solution  

    step 1: find all feasible_vertices from vertex v.
    step 2: from all the feasible vertex, choose one. backtrack 
            if no feasible vertex
    step 3: mark the chosen vertex as visited.
    step 4: repeat step 1,2,3 for the chosen vertex until we 
            visited all vertices.     
    step 5: if the last vertex in step 4 is not adjacent to the 
            starting vertex, backtrack and repeat step 1 to 4 
            until we find one. once found, make it a cycle, break 
            the loop and returns the solution. 
    """

    # base case, (step 5)
    if len(path) == 0:
        return False

    elif len(path) == len(graph): 
        if graph[entry][v]: # we can form a circle
            return path + [entry]
        else: # graph[entry][v] == 0, hamiltonian path only, not circle
            return []   
    
    # recursive steps
    solution = []

    # step 1: for current v, find all adjacent vertices that can be visited.
    next_move = feasible_vertices(graph,v,visited)

    for vertex in next_move: 
        new_path, new_visited = path[:],  [i[:] for i in visited]
        new_path.append(vertex)                 # step 2: pick one and append it to the path 
        new_visited[vertex][1]=True             # step 3: mark the chosen vertex as visited.
        cycle = backtracking(graph, entry, vertex, new_visited, new_path) # step 4: repeat step 1,2,3
        solution = solution  or cycle  # step 5: if cycle is formed, solution will be updated here
        if solution: # step5: break the loop if solution is already a cycle
            break
    
    return solution 


def hamiltonian_cycle(graph,entry): # [solution function]
    """
    input: a graph (adjacency matrix), and a starting vertex (entry)
    output: a hamiltonian cycle if found
    """
    visited = [[i,False] for i in range(len(graph))]
    visited[entry][1] = True
    path = backtracking(graph,entry,entry,visited,[entry])
    return path if path else "No valid Hamiltonian Cycle"



if __name__ == "__main__":

    graph1=[[0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
			[0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
			[0, 1, 1, 1, 0]]

    print (hamiltonian_cycle(graph1,0))

    graph2=[[0, 1, 0, 1, 0], 
            [1, 0, 1, 1, 1],
			[0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0],
			[0, 1, 1, 0, 0]]

    print (hamiltonian_cycle(graph2,0))


"""
graph1: 
    (0)--(1)--(2)
	|    / \   |
	|   /   \  |
	| /	     \ |
	(3)-------(4) 

graph2:
    (0)--(1)--(2)
	|    / \   |
	|   /   \  |
	| /	     \ |
	(3)       (4) 
"""
