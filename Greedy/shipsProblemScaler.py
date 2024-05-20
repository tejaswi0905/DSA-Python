import heapq

def min_solve(A, B, C):
    C.sort()
    total_amount = 0
    current_ship = 0
    while A > 0:
        current_tickets = C[current_ship]
        print(current_tickets)
        while current_tickets > 0:
            if A == 0:
                break
            total_amount += current_tickets
            current_tickets -= 1
            A -= 1
        current_ship += 1
    return total_amount

print(min_solve(10,5,[10,3,3,1,2]))

def max_solve(A,B,C):
    total = 0
    max_heap = []
    for ele in C:
        heapq.heappush(max_heap, -ele)
    while max_heap:
        if A == 0:
            break
        current_max = heapq.heappop(max_heap)
        total += -current_max
        current_max += 1
        if current_max != 0:
            heapq.heappush(max_heap, current_max)
        A -= 1

    return total
print(max_solve(4,3, [2,1,1]))



