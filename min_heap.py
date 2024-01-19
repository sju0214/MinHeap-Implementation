# Name: Seongyeong Ju
# OSU Email: jus@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 11/29/2023
# Description: MinHeap Implementation 


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds new object to MinHeap while maintaining heap property
        """
        self._heap.append(node)
        inserted_index = self.size() - 1
        parent_index = (inserted_index - 1) // 2
        while inserted_index > 0 and self._heap[inserted_index] < self._heap[parent_index]:
            # if value in parent index is greater than inserted index, swap
            temp = self._heap[inserted_index]
            self._heap[inserted_index] = self._heap[parent_index]
            self._heap[parent_index] = temp
            inserted_index = parent_index 
            parent_index = (inserted_index - 1) // 2

    def is_empty(self) -> bool:
        """
        Returns bool value of True if heap is empty and
        False if otherwise 
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Returns an object with minimum value of MinHeap without
        removing it and raises a MinHeapException if heap is empty 
        """
        if self._heap.length() == 0:
            raise MinHeapException
        return self._heap[0]

    def remove_min(self) -> object:
        """
        Removes minimum value from the heap and raises a MinHeapException
        if heap is empty 
        """
        if self.size() == 0:
            raise MinHeapException
        
        # save minimum value to return later 
        min_val = self.get_min()
        # replace first element value with last element value 
        self._heap[0] = self._heap[self.size() - 1]
        self._heap._size -= 1  # remove last element 

        _percolate_down(self._heap, 0, self._heap.length())

        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a proper MinHeap from given DynamicArray with objects in
        any order with current content overwritten 
        """
        self._heap = DynamicArray(da)
        parent_index = (self.size() // 2) - 1 # (i − 1) / 2
        while parent_index >= 0:
            _percolate_down(self._heap, parent_index, self._heap.length())
            parent_index -= 1

    def size(self) -> int:
        """
        Returns the number of items stored in the heap 
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the heap 
        """
        self._heap = DynamicArray()
    

def heapsort(da: DynamicArray) -> None:
    """
    Uses heapsort algorithm to sort Dynamic Array into non-ascending order
    Sorts the array in place without creating any data structures
    """
    parent_index = (da.length() // 2) - 1 # (i − 1) / 2
    while parent_index >= 0:
        _percolate_down(da, parent_index, da.length())
        parent_index -= 1

    k = da.length() - 1
    while k >= 0:
        # swap k with root 
        temp = da[k]
        da[k] = da[0]
        da[0] = temp
        # percolate down from root to k-1
        # decrement k by 1 
        _percolate_down(da, 0, k)
        k -= 1

def _percolate_down(da: DynamicArray, parent_index: int, length: int) -> None:
    """
    Helper function to percolate down the MinHeap
    """
    left_index = (2 * parent_index) + 1 # left child = 2 * i + 1
    right_index = (2 * parent_index) + 2 # right child = 2 * i + 2
    smallest = parent_index
    # if left child is less than the parent, assign as new smallest
    if left_index < length and da[left_index] < da[parent_index]:
        smallest = left_index
    # if right child is less than the smallest, assign as new smallest
    if right_index < length and da[right_index] < da[smallest]:
        smallest = right_index 
    # if the smallest is not the parent, swap the parent with smallest value
    if smallest != parent_index:
        temp = da[smallest]
        da[smallest] = da[parent_index]
        da[parent_index] = temp
        parent_index = smallest
        # call function recursively to keep percolating 
        _percolate_down(da, parent_index, length)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
