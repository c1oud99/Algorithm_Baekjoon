def max_continuous_meals():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    N = int(data[0])
    if N == 0:
        print(0)
        return

    records = []
    money_info = {}
    line_idx = 1

    # Reading the meal records
    for i in range(N):
        S, W, D, P = data[line_idx].split()
        W, D, P = int(W), int(D), int(P)
        records.append((S, W, D, P))
        line_idx += 1

    # Reading the money information
    for i in range(N):
        S, M = data[line_idx].split()
        M = int(M)
        money_info[S] = M
        line_idx += 1

    # Filter the records where the senior has enough money
    valid_meals = []
    for S, W, D, P in records:
        if money_info[S] >= P:
            valid_meals.append((W, D))

    # Sort the valid meals by week and day
    valid_meals.sort()

    # Calculate the maximum continuous days
    max_days = 0
    current_streak = 1

    for i in range(1, len(valid_meals)):
        prev_week, prev_day = valid_meals[i-1]
        curr_week, curr_day = valid_meals[i]

        if (curr_week == prev_week and curr_day == prev_day + 1) or (curr_week == prev_week + 1 and curr_day == 0 and prev_day == 6):
            current_streak += 1
        else:
            current_streak = 1

        max_days = max(max_days, current_streak)

    print(max_days)

# Function to execute when running the script
if __name__ == "__main__":
    max_continuous_meals()
