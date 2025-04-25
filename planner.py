import sys
from vaccum_world import VacuumWorld
from search_alg import uniform_cost_search, depth_first_search

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    
    algorithm = sys.argv[1]
    world_file = sys.argv[2]
    
    # Load the world
    world = VacuumWorld(world_file)
    
    # Run the appropriate search alg
    if algorithm == "uniform-cost":
        plan, nodes_generated, nodes_expanded = uniform_cost_search(world)
    elif algorithm == "depth-first":
        plan, nodes_generated, nodes_expanded = depth_first_search(world)
    else:
        print(f"Unknown algorithm: {algorithm}")
        sys.exit(1)
    
    # Print the results
    if plan:
        for action in plan:
            print(action)
        print(f"{nodes_generated} nodes generated")
        print(f"{nodes_expanded} nodes expanded")
    else:
        print("No solution found")

if __name__ == "__main__":
    main()