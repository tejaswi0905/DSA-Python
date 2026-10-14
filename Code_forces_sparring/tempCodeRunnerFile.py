import sys
from functools import lru_cache
import random

# ==========================================
# 1. The Optimized Logic (To Test)
# ==========================================
def solve_optimized(p, q):
    # This is the O(1) logic we want to verify
    # Condition: Bob wins if 3p >= 2q AND q > p
    if 3 * p >= 2 * q and q > p:
        return "Bob"
    else:
        return "Alice"

# ==========================================
# 2. The Brute Force Logic (Ground Truth)
# ==========================================
# We use memoization to cache results of states (p, q, turn)
# turn: 0 for Alice, 1 for Bob
@lru_cache(maxsize=None)
def solve_brute_force(p, q, turn):
    # Winning Condition:
    # If at ANY point p/q == 2/3, Bob wins immediately.
    if 3 * p == 2 * q:
        return "Bob"
    
    # Ending Condition:
    # Game ends at p=0, q=1. If we haven't hit 2/3 yet, Alice wins.
    if p == 0 and q == 1:
        return "Alice"

    # Possible moves
    moves = []
    if p > 0:
        moves.append((p - 1, q))
    if q > 1:
        moves.append((p, q - 1))

    # Determine outcomes of all possible moves
    outcomes = []
    for next_p, next_q in moves:
        outcomes.append(solve_brute_force(next_p, next_q, 1 - turn))

    if turn == 0:  # Alice's Turn
        # Alice wins if she can make *at least one* move that leads to her winning.
        if "Alice" in outcomes:
            return "Alice"
        else:
            return "Bob"
    else:  # Bob's Turn
        # Bob wins if he can make *at least one* move that leads to him winning.
        if "Bob" in outcomes:
            return "Bob"
        else:
            return "Alice"

# ==========================================
# 3. The Stress Test Loop
# ==========================================
def run_stress_test():
    print("Starting Stress Test...")
    print("Range: p [1, 50], q [2, 50]")
    
    # Increase recursion depth for deep game trees
    sys.setrecursionlimit(5000)
    
    cases_checked = 0
    
    # Iterate through small ranges where brute force is feasible
    for p in range(1, 51):
        for q in range(2, 51):
            
            # 1. Get Ground Truth
            ground_truth = solve_brute_force(p, q, 0) # 0 = Alice starts
            
            # 2. Get Optimized Result
            optimized_ans = solve_optimized(p, q)
            
            # 3. Compare
            if ground_truth != optimized_ans:
                print("\n[MISMATCH FOUND!]")
                print(f"Input: p={p}, q={q}")
                print(f"Brute Force says: {ground_truth}")
                print(f"Optimized says: {optimized_ans}")
                print("Logic is INCORRECT.")
                return # Stop immediately on error
            
            cases_checked += 1
            if cases_checked % 500 == 0:
                print(f"Checked {cases_checked} cases... OK")

    print(f"\nSUCCESS! Checked {cases_checked} cases. No mismatches found.")
    print("The logic holds for all small inputs.")

if __name__ == "__main__":
    run_stress_test()