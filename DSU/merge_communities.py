def test_case(capacities, queries):
    n = len(capacities) - 1  
    water_left = capacities[:]  
    parent = [i for i in range(n + 2)]  

    def find(x):
        if x > n:
            return x
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def fill(vessel, amount):
        while amount > 0:
            curr = find(vessel)
            if curr > n:
                break  # all remaining vessels are full
            can_fill = min(amount, water_left[curr])
            water_left[curr] -= can_fill
            amount -= can_fill
            if water_left[curr] == 0:
                parent[curr] = find(curr + 1)  # skip this full vessel in the future

    def print_filled(vessel):
        print(capacities[vessel] - water_left[vessel])

    for query in queries:
        if query[0] == 1:
            fill(query[1], query[2])
        else:
            print_filled(query[1])
def main():
    n = int(input())
    capacities = [0] + list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        query = list(map(int, input().split()))
        queries.append(query)
    test_case(capacities, queries)

main()