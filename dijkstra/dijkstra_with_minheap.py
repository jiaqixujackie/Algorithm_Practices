class Dijkstra_Algorithm:

    """
    This class uses Dijstra_Algorithm to find the shorest distance
    and path from the source node (s) to every node in the given 
    adjacency list. Priority Queue implemented using min_heap) is 
    the main data strucutre used in this class.
    
    Time Complexity: 
        __init__ method: O(V)
        dijkstra_distance method: O(E*logV)
    Space Complexity: 
        __init__ method: O(V) for both input and auxiliary
        dijkstra_distance method: O(V) auxiliary
    """
    
    def __init__(self, adj_list:list[list], s:int) -> None:
        """
        This method create 4 lists:
            1. initialise the distance of every node to inf, and
               finalise distance to the source node to 0.
            2. initialise a min_heap, based on distance the distance
            3. initialise a vertex list to keep track of the location 
               of each node in the min_heap.
            4. initialise the parent list to None for every node.

        Time Complexity: O(V)
            O(V) for creating each of the 4 lists 
        Space Complexity: O(V)
            O(V) for input parameters
            O(V) for each of the 4 lists
        """
        self.adj_lst = adj_list
        self.distance = self.initialise_distance(s)
        self.parent = [None]*len(adj_list)
        self.heap = self.create_heap(s)
        self.heapsize = len(self.heap)
        self.vertex = self.allocate_vertices()


    def __len__(self) -> int:
        """
        To get the size of the heap  
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.heapsize

    def is_empty(self) -> bool:
        """
        This function return True if the heap is empty, False otherwise.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.heapsize == 1


    def initialise_distance(self,s: int) -> list:
        """
        This function set distance from s to all other node as infinity.
        And only set the distance from s to s as 0.

        :param s: index of the source node. 
        :return: a list of dafault distance (inf) except list[s]=0.

        Time Complexity: O(V)
            O(V) for constructing the list
            O(1) for making distance_s to 0
        
        Space Complexity: O(V)
            O(1) for input parameter
            O(V) for distance list
        """
        dist = [inf]*len(self.adj_lst)
        dist[s]=0
        return dist


    def create_heap(self, s:int) -> list:
        """
        Initialise the min_heap. Since the intitial distance from 
        the source node to all other node are set to infitity, 
        we only need to make sure that the source node (s) is on 
        top of the min_heap.

        :param s: index of the source node.
        :result: a min_heap of nodes based on distance.

        Time Complexity: O(V)
            O(V): for a list of size E to construct the heap
            O(1): make sure the source is on top of the heap.
        Space Complexity: O(V)
            O(1): for the input parameter.
            O(V): for the min_heap list.
        """
        n = len(self.adj_lst)
        lst = [None] + [i for i in range(n)]
        lst[s+1], lst[1] = lst[1], lst[s+1]
        return lst
    

    def allocate_vertices(self) -> list:
        """
        find the position of each node in the min_heap.

        :return: a list, where list[i] represent the position of 
                 node i in the heap.
        
        Time Complexity: O(V)
            O(V): for initialise the list
            O(V): for find the allocating the position to each node. 
        Space Complexity: O(V)
            O(V): for the vertex list
            O(1): for some local variables of constanct space (i.e. 
                  variable i,v in the for loop)
        """
        n = len(self.adj_lst)
        lst = [None]*n
        for i in range(1,len(self.heap)):
            v = self.heap[i]
            lst[v] = i
        return lst


    def get_min(self) -> int:
        """
        remove the node with the smallest distance from self.heap
        then re-heapify the heap, by distance.

        :return: the index of the removed node.

        Time Complexity: O(log V)
            O(1): for swap and removal
            O(log V): for heapify the heap
        Space Complexity: O(1), also in-place auxiliary.
        """
        if self.is_empty():
            raise ValueError("heap is empty")
        n = len(self)
        node0,node1 = self.heap[1], self.heap[len(self)-1]  # get the root and last node
        self.vertex[node0] = -1                             # pop the root node 
        self.vertex[node1], self.heap[1] = 1, node1         # update the last node's location in heap
        
        self.heapsize -= 1
        self.sink(1)
        return node0
    

    def sink(self, k) -> None:
        """
        heapify self.heap by swapping kth node with its child node if
        the child has smaller distance than the kth node in the heap.

        :param k: an index representing the kth node on the heap. 

        Time Complexity: O(log V)
            O(V): for V swaps, occured when the kth node has the longest 
                  distance, so it needs to be sink to the bottom.
        Space Complexity: O(1), in-place auxililary
            O(1): for input parameter
            O(1): for all the local variables.
        """
        while 2*k <= self.heapsize: # while this node has child
            n1 = self.heap[k]
            d1 = self.distance[n1]
            k2,d2 = self.smaller_child(k)
            if d1 <= d2:
                break
            self.swap(k, k2)
            k = k2


    def swap(self, k1:int, k2:int) -> None:
        """
        swap two nodes in the heap and update the self.vertex list.

        :param k1: position of the first node in the heap
        :param k2: position of the second node in the heap

        Time complexity: O(1)
        Space complexity: O(1)
        """
        node1, node2 = self.heap[k1], self.heap[k2]
        self.heap[k1], self.heap[k2] = node2, node1
        self.vertex[node1], self.vertex[node2] = k2, k1


    def smaller_child(self,k:int) -> tuple:
        """
        for node k in the heap, this function compare the child/children
        of node k and returns the smaller one with its distance.

        :param k: index of a node in the min heap (k-th node)
        :return: smaller child's position in heap and its corresponding 
                 distance.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if 2*k == len(self):
            node = self.heap[2*k]
            dist = self.distance[node]
            return (2*k, dist)
        
        left_index, right_index = 2*k, 2*k+1
        left_node, right_node = self.heap[2*k], self.heap[2*k+1]
        left_dist, right_dist = self.distance[left_node], self.distance[right_node]

        if left_dist < right_dist:
            return (left_index, left_dist)
        else: # right_dist >= left_dist:
            return (right_index, right_dist)


    def raise_up(self,k:int) -> None:
        """
        for a given node k in the min heap, if node k's distance is smaller
        than its parent, then consecutively swap node k with its parent(s) 
        until it's distance becomes greater or equal to its parent. 

        :param k: position of a node in the min heap

        Time Complexity: O(log V)
            O(1): access node k, its parent, and their distance
            O(log V) swaps in worst case, that is, swap the k-th node from
                     the bottom to the top of the min heap. 
        Space Complexity: O(1)
        """
        while k!=1:
            k2 = k//2
            node, node2 = self.heap[k], self.heap[k2]
            dist, dist2 = self.distance[node], self.distance[node2]
            if dist >= dist2:
                break
            self.swap(k, k2)
            k = k//2

    def dijkstra_distance(self) -> list:
        """
        find the shortest path from the source node (root of the self.heap)
        to all other nodes in the heap. 

        Approach: Greedy Approach Using the Dijkstra Algorithm.

        :return: a list (distance) where distance[i] indicates the shortest 
                 distance from the source node to node i; with another list 
                 (parent) where parent[i] represents the visited node before
                 node i is visited in the path.  
        
        Time Complexity: O(V*logV + E*logV) ≈ O(max(V,E) * logV) ≈ O(E*logV)
            O(V*logV): for visiting each node once (get_min() is O(logV), we 
                       called get_min() V times to visit every nodes).
            O(E*logV): for relax every edge exactly once, and update the min_heap
        Space Complexity: O(V)
            O(1) for local variables.
            O(2V) for returned variables self.distance and self.parent
        """
        while not self.is_empty():
            u = self.get_min()
            for v,w in self.adj_lst[u]:
                if self.vertex[v] != -1:
                    old_dist = self.distance[v]
                    new_dist = self.distance[u] + w
                    if new_dist < old_dist:
                        self.distance[v], self.parent[v] = new_dist, u
                        self.raise_up(self.vertex[v])
        return self.distance, self.parent