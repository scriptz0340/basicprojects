import sys
import time  # For animation delays
import os    # For clearing the screen


# Represents a single node in the search tree
class Node():
    
    def __init__(self, state, parent, action):
        self.state = state      # Current position in the maze (row, col)
        self.parent = parent    # Parent Node from which we came
        self.action = action    # Action taken to reach this node


# Stack-based frontier (LIFO) for depth-first search
class StackFrontier():
    
    def __init__(self):
        self.frontier = []  # List to store nodes to be explored
    
    def add(self, node):
        self.frontier.append(node)  # Add node to the end of the list

    def contains_state(self, state):
        # Check if a state is already in the frontier
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        # Return True if frontier is empty
        return len(self.frontier) == 0
    
    def remove(self):
        # Remove and return the last node (DFS behavior)
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        

# Queue-based frontier (FIFO) for breadth-first search
class QueueFrontier(StackFrontier):

    def remove(self):
        # Remove and return the first node (BFS behavior)
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


# Maze class that handles loading, parsing, solving, and printing the maze
class Maze():

    def __init__(self, filename):

        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one goal")
        
        # Determine height and width of maze
        contents = contents.splitlines()  # Split file into lines
        self.height = len(contents)       # Number of rows
        self.width = max(len(line) for line in contents)  # Longest line = width

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)  # Store start position
                        row.append(False)   # Start is not a wall
                    elif contents[i][j] == "B":
                        self.goal = (i, j)   # Store goal position
                        row.append(False)   # Goal is not a wall
                    elif contents[i][j] == " ":
                        row.append(False)   # Open path
                    else:
                        row.append(True)    # Wall
                except IndexError:
                    row.append(False)       # If line is too short, treat as empty
            self.walls.append(row)          # Add row to wall grid

        self.solution = None  # Will hold the final path (actions, cells)

    
    def print(self):
        # Display the maze with solution path if available
        solution = self.solution[1] if self.solution is not None else None
        os.system("cls" if os.name == "nt" else "clear")  # Clear the screen

        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    # Wall visualization using █
                    print("█", end="")
                elif (i, j) == self.start:
                    # Print start
                    print("A", end="")
                elif (i, j) == self.goal:
                    # Print goal
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    # Print part of the solution path
                    print("*", end="")
                else:
                    # Print empty space
                    print(" ", end="")
            print()  # Newline after each row
        print()

    
    def neighbors(self, state):
        # Returns a list of (action, state) tuples for neighboring cells
        row, col = state

        # All possible actions
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        # Ensure actions are within bounds and not into walls
        result = []
        for action, (r, c) in candidates:
            try:
                if not self.walls[r][c]:  # Valid move
                    result.append((action, (r, c)))
            except IndexError:
                continue  # Ignore out-of-bounds
        return result
    
    
    def solve(self):
        """Finds a solution to maze, if one exists."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)

        # DFS by default: use StackFrontier
        frontier = StackFrontier()

        # To use BFS instead, switch to:
        # frontier = QueueFrontier()

        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()
        
        # Keep looping until solution is found or no nodes left
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")
            
            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # TEMPORARY: show current path to this node for animation
            temp_path = []
            trace = node
            while trace.parent is not None:
                temp_path.append(trace.state)
                trace = trace.parent
            temp_path.reverse()

            self.solution = (None, temp_path)  # Temporarily store current path
            self.print()
            time.sleep(.05)  # Delay for animation (adjust for speed)

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []

                # Follow parent nodes to find solution path
                while node.parent is not None:
                    actions.append(node.action)     # Action taken to reach this cell
                    cells.append(node.state)       # Cell visited
                    node = node.parent
                actions.reverse()  # Reverse to get correct order
                cells.reverse()
                self.solution = (actions, cells)  # Store solution
                return
            
            # Mark node as explored 
            self.explored.add(node.state)

            # Add neighbors to the frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)


# Example usage:
# To run the maze solver, use the following block:
# (Make sure to have maze1.txt, maze2.txt, or maze3.txt in the same directory)

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "maze1.txt"  # Get filename from args or use default
    m = Maze(filename)
    print("Solving...")
    m.solve()
    m.print()
    print(f"States Explored: {m.num_explored}")
