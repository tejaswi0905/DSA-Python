def solve(n, k, g):
    total_coins = k * g
    max_save = (g - 1) // 2
    
    # Give max_save to as many people as possible
    stolen = min(max_save * n, total_coins)
    
    # Calculate remaining after this distribution
    remaining = (total_coins - stolen) % g
    
    if remaining > 0:
        # Take back max_save from one person
        stolen -= max_save
        
        # Give them max_save + remaining instead
        last_person_total = max_save + remaining
        last_remainder = last_person_total % g
        
        # Check if it rounds down or up
        if last_remainder * 2 < g:
            stolen += last_remainder
        else:
            stolen -= (g - last_remainder)
    
    return stolen

def main():
    t = int(input())
    for _ in range(t):
        n, k, g = list(map(int, input().split()))
        print(solve(n, k, g))
main()