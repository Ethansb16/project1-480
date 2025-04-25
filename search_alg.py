import heapq

def uniform_cost_search(world):
    directions = [(-1, 0, 'N'), (0, 1, 'E'), (1, 0, 'S'), (0, -1, 'W')]
    
    # Initial state: (robot_row, robot_col, frozenset(dirty_cells) frozen so that it's hashable)
    start_pos = world.robot_pos
    start_state = (start_pos[0], start_pos[1], frozenset(world.dirty_cells))
    
    # Priority queue for UCS (cost, state, path, count)
    pq = [(0, start_state, [], 0)]
    
    visited = set()
    
    # Counters 
    nodes_generated = 1
    nodes_expanded = 0
    
    while pq:
        # Get the lowest cost state
        cost, state, path, _ = heapq.heappop(pq)
        robot_r, robot_c, dirty_cells = state
        
        if state in visited:
            continue
        
        # Mark as visited, increment expanded counter
        visited.add(state)
        nodes_expanded += 1
        
        # Check if no more dirty cells
        if not dirty_cells:
            return path, nodes_generated, nodes_expanded
        
        # Check if current position is dirty 
        if (robot_r, robot_c) in dirty_cells:
            # Vacuum the dirty cell
            new_dirty_cells = set(dirty_cells)
            new_dirty_cells.remove((robot_r, robot_c))
            new_state = (robot_r, robot_c, frozenset(new_dirty_cells))
            
            # Add the new state to the pq with increased cost
            nodes_generated += 1
            heapq.heappush(pq, (cost + 1, new_state, path + ['V'], nodes_generated))
        
        # Try all four directions
        for dr, dc, action in directions:
            new_r, new_c = robot_r + dr, robot_c + dc
            
            # Check if move is valid
            if world.is_valid_move(new_r, new_c):
                new_state = (new_r, new_c, dirty_cells)
                
                # Add the new state to the pq 
                nodes_generated += 1
                heapq.heappush(pq, (cost + 1, new_state, path + [action], nodes_generated))
    
    # no solution was found
    return None, nodes_generated, nodes_expanded

# Depth-First Search
def depth_first_search(world):
    directions = [(-1, 0, 'N'), (0, 1, 'E'), (1, 0, 'S'), (0, -1, 'W')]
    
    # Initial state: (robot_row, robot_col, frozenset(dirty_cells))
    start_pos = world.robot_pos
    start_state = (start_pos[0], start_pos[1], frozenset(world.dirty_cells))
    
    # Stack for DFS (state, path)
    stack = [(start_state, [])]
    
    visited = set()
    
    # Counters 
    nodes_generated = 1
    nodes_expanded = 0
    
    while stack:
        # Get the next state from the stack 
        state, path = stack.pop()
        robot_r, robot_c, dirty_cells = state
        
        # Check if we've already visited this state
        if state in visited:
            continue
        
        # Mark as visited, increment expanded counter
        visited.add(state)
        nodes_expanded += 1
        
        # Check if no more dirty cells 
        if not dirty_cells:
            return path, nodes_generated, nodes_expanded
        
        # Check if current position is dirty 
        if (robot_r, robot_c) in dirty_cells:
            # Vacuum the dirty cell
            new_dirty_cells = set(dirty_cells)
            new_dirty_cells.remove((robot_r, robot_c))
            new_state = (robot_r, robot_c, frozenset(new_dirty_cells))
            
            # Add the new state to the stack
            nodes_generated += 1
            stack.append((new_state, path + ['V']))
        
        # Try all four directions in reverse order
        for dr, dc, action in reversed(directions):
            new_r, new_c = robot_r + dr, robot_c + dc
            
            # Check if move is valid
            if world.is_valid_move(new_r, new_c):
                new_state = (new_r, new_c, dirty_cells)
                
                # Add the new state to the stack
                nodes_generated += 1
                stack.append((new_state, path + [action]))
    
    # no solution was found
    return None, nodes_generated, nodes_expanded