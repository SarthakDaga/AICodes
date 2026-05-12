n = int(input("Enter the size of the board (n): "))

def solve(q=()):
    if n in [2, 3]:
        return print(f"No solution exists for n={n}")

    if len(q) == n:
        [print("_ "*i + "Q " + "_ "*(n-i-1)) for i in q]
        return print()

    for c in range(n):
        if all(c != v and abs(c - v) != len(q) - i for i, v in enumerate(q)):
            solve(q + (c,))

solve()
