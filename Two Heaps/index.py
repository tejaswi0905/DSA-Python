# import heapq as hq


# class MinHeap:
#     def __init__(self):
#         self.heap = []

#     def insert(self, value):
#         hq.heappush(self.heap, value)

#     def pop(self):
#         value = hq.heappop(self.heap)
#         return value

#     def peak(self):
#         return self.heap[0]

#     def length(self):
#         return len(self.heap)

#     def is_empty(self):
#         return len(self.heap) == 0


# class MaxHeap:
#     def __init__(self):
#         self.heap = []

#     def insert(self, value):
#         value = -1 * value
#         hq.heappush(self.heap, value)

#     def pop(self):
#         value = hq.heappop(self.heap)
#         value = -1 * value
#         return value

#     def peak(self):
#         value = self.heap[0]
#         return (-1) * value

#     def length(self):
#         return len(self.heap)

#     def is_empty(self):
#         return len(self.heap) == 0


# def balance_heaps(min_heap, max_heap):
#     if min_heap.length() > max_heap.length() and abs(min_heap.length() - max_heap.length() == 2):
#         value = min_heap.pop()
#         max_heap.insert(value)

#     elif max_heap.length() > min_heap.length() and abs(min_heap.length() - max_heap.length() == 2):
#         value = max_heap.pop()
#         min_heap.insert(value)


# def find_median(min_heap, max_heap):
#     if min_heap.length() == max_heap.length():
#         median = (min_heap.peak() + max_heap.peak())/2
#     elif min_heap.length() > max_heap.length():
#         min_heap.length() - max_heap.length() <= 1
#         median = min_heap.peak()
#     elif max_heap.length() > min_heap.length():
#         max_heap.length() - min_heap.length() <= 1
#         median = max_heap.peak()
#     return median


# def solve(array):
#     min_heap = MinHeap()
#     max_heap = MaxHeap()
#     ans = []
#     max_heap.insert(array[0])
#     for i in range(1, len(array)):
#         val = array[i]
#         if val == 0:
#             ans.append(find_median(min_heap, max_heap))
#         else:
#             m = find_median(min_heap, max_heap)
#             if val < m:
#                 max_heap.insert(val)
#             else:
#                 min_heap.insert(val)
#             if abs(min_heap.length() - max_heap.length()) == 2:
#                 balance_heaps(min_heap, max_heap)
#     return ans


# def sliding_window_median(arr, k):
#     n = len(arr)

#     min_heap = MinHeap()
#     max_heap = MaxHeap()
#     ans = []
#     delayed = {}

#     def prune_min():
#         while not min_heap.is_empty():
#             num = min_heap.peak()
#             if num in delayed and delayed[num] > 0:
#                 delayed[num] -= 1
#                 min_heap.pop()
#             else:
#                 break

#     def prune_max():
#         while not max_heap.is_empty():
#             num = max_heap.peak()
#             if num in delayed and delayed[num] > 0:
#                 delayed[num] -= 1
#                 max_heap.pop()
#             else:
#                 break

#     def add(num):
#         if max_heap.is_empty() or num <= max_heap.peak():
#             max_heap.insert(num)
#         else:
#             min_heap.insert(num)

#     def remove(num):
#         delayed[num] = delayed.get(num, 0) + 1
#         # check which side the num belongs to
#         if not max_heap.is_empty() and num <= max_heap.peak():
#             if num == max_heap.peak():
#                 prune_max()
#         else:
#             if not min_heap.is_empty() and num == min_heap.peak():
#                 prune_min()
#     left = 0
#     for right in range(len(arr)):
#         num = arr[right]
#         add(num)
#         prune_max()
#         prune_min()
#         balance_heaps(min_heap, max_heap)

#         if right - left + 1 == k:
#             prune_max()
#             prune_min()

#             ans.append(find_median(min_heap, max_heap))
#             remove(arr[left])
#             left += 1

#             prune_min()
#             prune_max()
#             balance_heaps(min_heap, max_heap)
#     return ans

import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)

    def peak(self):
        return self.heap[0]

    def length(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peak(self):
        return -self.heap[0]

    def length(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


# ---------- PRUNE ----------
def prune_max(max_heap, delayed):
    while not max_heap.is_empty():
        num = max_heap.peak()
        if num in delayed and delayed[num] > 0:
            delayed[num] -= 1
            max_heap.pop()
        else:
            break


def prune_min(min_heap, delayed):
    while not min_heap.is_empty():
        num = min_heap.peak()
        if num in delayed and delayed[num] > 0:
            delayed[num] -= 1
            min_heap.pop()
        else:
            break


# ---------- BALANCE ----------
def balance_heaps(min_heap, max_heap):
    if max_heap.length() > min_heap.length() + 1:
        min_heap.insert(max_heap.pop())

    elif min_heap.length() > max_heap.length():
        max_heap.insert(min_heap.pop())


# ---------- MEDIAN ----------
def find_median(min_heap, max_heap):
    if max_heap.length() == min_heap.length():
        return (max_heap.peak() + min_heap.peak()) / 2
    return max_heap.peak()


# ---------- MAIN ----------
def solve(arr, k):
    min_heap = MinHeap()
    max_heap = MaxHeap()
    delayed = {}
    result = []

    def add(num):
        if max_heap.is_empty() or num <= max_heap.peak():
            max_heap.insert(num)
        else:
            min_heap.insert(num)

    def remove(num):
        delayed[num] = delayed.get(num, 0) + 1

        # # optional immediate prune (helps cleanliness)
        # if not max_heap.is_empty() and num == max_heap.peak():
        #     prune_max(max_heap, delayed)
        # elif not min_heap.is_empty() and num == min_heap.peak():
        #     prune_min(min_heap, delayed)

    left = 0

    for right in range(len(arr)):
        # 1. ADD
        add(arr[right])

        # 2. CLEAN before balancing
        prune_max(max_heap, delayed)
        prune_min(min_heap, delayed)

        # 3. BALANCE
        balance_heaps(min_heap, max_heap)

        # 4. WINDOW READY
        if right - left + 1 == k:

            # CLEAN before median
            prune_max(max_heap, delayed)
            prune_min(min_heap, delayed)

            # 5. GET MEDIAN
            result.append(find_median(min_heap, max_heap))

            # 6. REMOVE outgoing
            remove(arr[left])
            left += 1

            # CLEAN before balancing again
            prune_max(max_heap, delayed)
            prune_min(min_heap, delayed)

            # 7. BALANCE again
            balance_heaps(min_heap, max_heap)

    return result


arr = [1, 2, -1, 3, 5]
k = 2
print(solve(arr, k))
