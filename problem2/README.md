# 🐱 Emoji Maze Escape
# This Python program finds the shortest path for a cat (🐱) to escape a maze full of emojis.

# Emoji Legend:
# 🐱 : Starting Point
# 🚪 : Exit
# 🟩 : Path
# 🟥 : Wall

# How It Works:
# 1. The maze is represented as a 2D Python list called `grid`.
# 2. The program locates the cat's starting position.
# 3. It uses Breadth-First Search (BFS) to explore the maze:
#    - Moves are allowed up, down, left, right.
#    - Walls (🟥) cannot be crossed.
# 4. BFS guarantees the shortest path is found.
# 5. The program prints the path as a list of coordinates from start to exit.

# Example grid:
grid = [
    ["🐱", "🟩", "🟥", "🟩"],
    ["🟩", "🟩", "🟥", "🟩"],
    ["🟥", "🟩", "🟩", "🟩"],
    ["🟩", "🟩", "🟥", "🚪"]
]

# Output for the above grid:
# [(0,0), (0,1), (1,1), (2,1), (2,2), (2,3), (3,3)]

# How to Use:
# 1. Copy your maze into the `grid` variable.
# 2. Run the program.
# 3. The shortest path from 🐱 to 🚪 will be printed.

# Notes:
# - The grid can be any size.
# - If there is no possible path, the program should return -1 or an empty list.
# - The program can be extended with multiple cats, multiple exits, traps, or moving walls.
