from collections import deque

def goalTest(state, goal):
    # Goal is achieved if any jug has the target amount
    return state[0] == goal or state[1] == goal


def getSuccessors(state, cap1, cap2):
    x, y = state
    successors = []

    # Fill jugs
    successors.append((cap1, y))
    successors.append((x, cap2))

    # Empty jugs
    successors.append((0, y))
    successors.append((x, 0))

    # Pour Jug1 -> Jug2
    transfer = min(x, cap2 - y)
    successors.append((x - transfer, y + transfer))

    # Pour Jug2 -> Jug1
    transfer = min(y, cap1 - x)
    successors.append((x + transfer, y - transfer))

    return successors


def waterJug(cap1, cap2, goal):
    start = (0, 0)
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        state = queue.popleft()

        if goalTest(state, goal):
            # Print path
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            path.reverse()

            print("\nSolution Path:")
            for step in path:
                print(step)
            return

        for next_state in getSuccessors(state, cap1, cap2):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = state
                queue.append(next_state)

    print("\nNo solution exists.")


# -------- Main Program --------
if __name__ == "__main__":
    cap1 = int(input("Enter capacity of Jug 1: "))
    cap2 = int(input("Enter capacity of Jug 2: "))
    goal = int(input("Enter goal amount: "))

    waterJug(cap1, cap2, goal)
