# MinHeap Implementation

### Overview

This repository contains the implementation of the MinHeap class using a DynamicArray, as specified in the provided skeleton code (min_heap.py). The MinHeap class includes essential methods for heap operations, such as add(), is_empty(), get_min(), remove_min(), build_heap(), size(), clear(), and heapsort().


### Implementation Details

The main implementation is provided in the file min_heap.py. It includes a skeleton code that you need to complete by implementing the following methods:

- `add()`: Adds a new object to the MinHeap while maintaining heap property in O(log N)
- `is_empty()`: Returns True if the heap is empty, otherwise, returns False in O(1)
- `get_min()`: Returns an object with the minimum key, without removing it from the heap. If heap is empty, a MinHeapException is raised in O(1)
- `remove_min()`: Returns an object with the minimum key, and removes it from the heap. If heap is empty, a MinHeapException is raised in O(log N)
- `clear()`: Clears the contents of the heap in O(1)
- `build_heap()`: Receives a DynamicArray with objects in any order, and builds a proper MinHeap from them with the current contents overwritten in O(N)
- `size()`: Returns number of items currently stored in the heap in O(1)
- `heapsort()`: Receives a DynamicArray and sorts its content in non-ascending order, using the Heapsort algorithm in O(N log N)

1. The MinHeap must be implemented with a DynamicArray as per the skeleton code. My existing DynamicArray has been used for this MinHeap implementation. 
2. All methods must meet optimized runtime requirements. 
3. The number of objects stored in the minheap will be between 0 and 1,000,000 inclusive.
4. RESTRICTIONS: Any variables of the DynamicArray class are NOT allowed to be directly accessed. All work must be done only by using class methods. 
5. RESTRICTIONS: ANY built-in Python data structures and/or their methods must NOT be used.

