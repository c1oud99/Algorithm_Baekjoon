def select_participants(participants):
    filtered_participants = []

    for participant in participants:
        name, status, icpc, shake_rank, apc_rank = participant

        # 재학 중
        if status != "jaehak":
            continue

        # ICPC 수상자X
        if icpc == "winner":
            continue

        # shake! 3위 이내X
        if 1 <= shake_rank <= 3:
            continue

        filtered_participants.append(participant)

    filtered_participants.sort(key=lambda x: x[4])
    selected_participants = filtered_participants[:10]
    selected_participants_names = sorted([participant[0] for participant in selected_participants])

    return selected_participants_names


n = int(input().strip())
participants = []

for _ in range(n):
    data = input().strip().split()
    name = data[0]
    status = data[1]
    icpc = data[2]
    shake_rank = int(data[3])
    apc_rank = int(data[4])
    participants.append((name, status, icpc, shake_rank, apc_rank))


result = select_participants(participants)

print(len(result))
for name in result:
    print(name)
