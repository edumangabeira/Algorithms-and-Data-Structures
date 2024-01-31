from typing import Any, List

class PriorityQueue():
    def __init__(self, S: List) -> None:
        self.S = list(set(S))

    def insert(self, element: Any):
        '''
        insert element x into set S
        '''
        self.S.append(element)

    def max(self):
        '''
        return element of S with largest key
        '''
        return self.S[-1]

    def min(self):
        '''
        return element of S with smallest key
        '''
        return self.S[0]
    
    def extract_max(self):
        '''
        return element of S with largest key and remove it from S
        '''
        max_element = self.S[-1]
        self.S.pop(-1)
        return max_element

    def extract_min(self):
        '''
        return element of S with smallest key and remove it from S
        '''
        min_element = self.S[0]
        self.S.pop(0)
        return min_element

    def increase_key(self, new_key, element):
        '''
        increase the value of element's key 'current_key'
        to new value 'new_key'
        (assumed to be as large as current value)
        '''
        current_key = self.S.index(element)
        if new_key >= current_key:
            self.S[current_key] = self.S[new_key]
            self.S[new_key] = element

        else:
            raise Exception("""
            The value of the new key is supposed 
            to be as large as current value
        """)


class Heap(PriorityQueue):
    '''
    - Implementation of a priority queue
    - An array, visualized as a nearly complete binary tree
    - Max Heap Property: The key of a node is ≥ than the keys of its children
    (Min Heap defined analogously)
    '''
    def __init__(self, S: List) -> None:
        '''
        Heap as a Tree
        root of tree: first element in the array, corresponding to i = 1 
        '''
        super().__init__(S)
        self.tree_root = S[0]

    def parent(self, i):
        '''
        parent(i) = i/2: returns index of node's parent
        '''
        return i//2
    
    def left(self, i):
        '''
        left(i)=2i: returns index of node's left child
        '''
        return 2*i

    def right(self, i):
        '''
        right(i)=2i+1: returns index of node's right child
        '''
        return (2*i)+1

    def max_heapify(self):
        '''
        correct a single violation of the heap property in a subtree at its root.
        - Assume that the trees rooted at left(i) and right(i) are max-heaps
        - If element A[i] violates the max-heap property, correct violation by 
        "trickling" element A[i] down the tree, making the subtree rooted 
        at index i a max-heap


        Pseudocode:

        l = left(i)
        r = right(i)
        if (l <= heap-size(A) and A[l] > A[i])
        then largest = l else largest = i
        if (r <= heap-size(A) and A[r] > A[largest])
        then largest = r if largest = i
        then exchange A[i] and A[largest]
        Max_Heapify(A, largest)
        '''
        raise NotImplemented

    def build_max_heap(self):
        '''
        produce a max-heap from an unordered array

        Pseudocode:
        Converts A[1...n] to a max heap
        Build_Max_Heap(A): for i=n/2 downto 1
        do Max_Heapify(A, i)
        '''
        raise NotImplemented

