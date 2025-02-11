from collections import deque

def move_box(warehouse):
    length = 10
    robot_pos = warehouse.index('@')
    box_pos = warehouse.index('#')
    goal_pos = warehouse.index('!')

    queue = deque([(robot_pos, box_pos, 0)])
    visited = set()
    visited.add((robot_pos, box_pos))

    while queue:
        robot, box, moves = queue.popleft()

        for direction in [-1, 1]:
            new_robot_pos = robot + direction

            if 0 <= new_robot_pos < length:
                if new_robot_pos == box:
                    new_box_pos = box + direction

                    if 0 <= new_box_pos < length and warehouse[new_box_pos] in '.!':
                        if new_box_pos == goal_pos:
                            return moves + 1
                        if (new_robot_pos, new_box_pos) not in visited:
                            visited.add((new_robot_pos, new_box_pos))
                            queue.append((new_robot_pos, new_box_pos, moves + 1))

                elif warehouse[new_robot_pos] == '.':
                    if (new_robot_pos, box) not in visited:
                        visited.add((new_robot_pos, box))
                        queue.append((new_robot_pos, box, moves + 1))

    return -1

warehouse = input().strip()

result = move_box(warehouse)
print(result)
