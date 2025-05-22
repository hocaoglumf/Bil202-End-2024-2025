import tkinter as tk
import random

# Symbols
AGENT = "🧍"
WUMPUS = "👹"
PIT = "🕳️"
GOLD = "💰"
BREEZE = "🌀"
STENCH = "💩"
EMPTY = ""

GRID_SIZE = 10
NUM_PITS = 10

class WumpusWorldGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wumpus World 10x10")
        self.grid = [[[] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.buttons = []

        self.place_objects()
        self.add_percepts()
        self.create_grid()

    def place_objects(self):
        positions = random.sample([(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE)], NUM_PITS + 3)

        # Pits
        for pos in positions[:NUM_PITS]:
            i, j = pos
            self.grid[i][j].append(PIT)

        # Wumpus
        self.wumpus_pos = positions[NUM_PITS]
        self.grid[self.wumpus_pos[0]][self.wumpus_pos[1]].append(WUMPUS)

        # Gold
        i, j = positions[NUM_PITS + 1]
        self.grid[i][j].append(GOLD)

        # Agent
        i, j = positions[NUM_PITS + 2]
        self.grid[i][j].append(AGENT)

    def add_percepts(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if PIT in self.grid[i][j]:
                    for ni, nj in self.get_adjacent(i, j):
                        if BREEZE not in self.grid[ni][nj]:
                            self.grid[ni][nj].append(BREEZE)
                if WUMPUS in self.grid[i][j]:
                    for ni, nj in self.get_adjacent(i, j):
                        if STENCH not in self.grid[ni][nj]:
                            self.grid[ni][nj].append(STENCH)

    def get_adjacent(self, i, j):
        neighbors = []
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE:
                neighbors.append((ni, nj))
        return neighbors

    def create_grid(self):
        for i in range(GRID_SIZE):
            row_buttons = []
            for j in range(GRID_SIZE):
                content = ''.join(self.grid[i][j])
                cell = tk.Button(
                    self.root,
                    text=content,
                    font=("Arial", 14),
                    width=5,
                    height=2,
                    command=lambda x=i, y=j: self.on_cell_click(x, y)
                )
                cell.grid(row=i, column=j, padx=2, pady=2)
                row_buttons.append(cell)
            self.buttons.append(row_buttons)

    def on_cell_click(self, row, col):
        content = ''.join(self.grid[row][col])
        print(f"Clicked ({row},{col}): {content}")

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = WumpusWorldGUI(root)
    root.mainloop()
