goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  

def is_goal(state):
    return state == goal_state

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def swap(state, i1, j1, i2, j2):
    new_state = [row[:] for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return new_state

def get_neighbors(state):
    neighbors = []
    i, j = find_blank(state)
    
    if i > 0:
        neighbors.append(swap(state, i, j, i - 1, j))
    if i < 2:  
        neighbors.append(swap(state, i, j, i + 1, j))
    if j > 0:  
        neighbors.append(swap(state, i, j, i, j - 1))
    if j < 2:  
        neighbors.append(swap(state, i, j, i, j + 1))
    
    return neighbors

def dfs(state, visited, path):

    state_tuple = tuple(tuple(row) for row in state)

    if state_tuple in visited:
        return None
    visited.add(state_tuple)


    if is_goal(state):
        return path

    for neighbor in get_neighbors(state):
        result = dfs(neighbor, visited, path + [neighbor])
        if result is not None:
            return result
    
    return None

initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

visited = set()
solution = dfs(initial_state, visited, [])

if solution:
    print("Solution found in", len(solution), "steps:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")