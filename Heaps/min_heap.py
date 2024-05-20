class Min_heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child_index(self, i, len_heap):
        left_child_idx = (2 * i) + 1
        if left_child_idx < len_heap:
            return left_child_idx
        else:
            return None

    def right_child_index(self, i, len_heap):
        right_child_idx = (2 * i) + 2
        if right_child_idx < len_heap:
            return right_child_idx
        else:
            return None
    # The way inserting works is, we append the node at the end and store the idx of the node as i, we keep
    # checking if this new node valus is less than its parent node, if so we swith, if not we stop.

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        parent_idx = self.parent(i)
        while i > 0 and(self.heap[i] < self.heap[parent_idx]):
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i];
            i = parent_idx
            parent_idx = self.parent(parent_idx)

    def min_heapify_at_idx(self, i, array):
        n = len(array)
        smallest = i
        l = self.left_child_index(i, n)
        r = self.right_child_index(i, n)

        if(l is not None) and (array[l] < array[smallest]):
            smallest = l
        if (r is not None) and (array[r] < array[smallest]):
            smallest = r

        if (smallest != i):
            array[i], array[smallest] = array[smallest], array[i]
            self.min_heapify_at_idx(smallest, array)

    def min_heapify(self, array):
        n = len(array)
        last_non_leaf_node = (n - 1) // 2
        for i in range(last_non_leaf_node, -1, -1):
            self.min_heapify_at_idx(i, array)

    def extarct_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        last = self.heap.pop()
        self.heap[0] = last
        self.min_heapify_at_idx(0, self.heap)
        return root




min_heap = Min_heap()
min_heap.heap = [5, 9, 11, 14, 18, 19, 21]
min_heap.insert(13)
print(min_heap.heap)
min_element = min_heap.extarct_min()
print(min_element)
print(min_heap.heap)