def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits

        if total_legs == numlegs:
            return num_chickens, num_rabbits

    return None, None

numheads = 35
numlegs = 94
result_chickens, result_rabbits = solve(numheads, numlegs)

if result_chickens is not None:
    print(f"There are {result_chickens} chickens and {result_rabbits} rabbits.")
else:
    print("No solution found.")
