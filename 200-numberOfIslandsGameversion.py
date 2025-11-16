import tkinter as tk
from tkinter import messagebox

class IslandGame:
    def __init__(self, root, grid):
        self.root = root
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.buttons = []
        self.island_count = 0
        
        self.build_ui()

    def build_ui(self):
        self.root.title("Island Hunter Game")

        #label for score
        self.label = tk.Label(self.root, text="Islands Found: 0", font=("Arial", 14))
        self.label.pack()

        # frame for grid
        frame = tk.Frame(self.root)
        frame.pack()

        # create buttons for each cell
        for r in range(self.rows):
            row_buttons = []
            for c in range(self.cols):
                btn = tk.Button(
                    frame, 
                    text=self.grid[r][c], 
                    width=4, height=2,
                    bg="lightgray",
                    command=lambda x=r, y=c: self.on_click(x, y)
                )
                btn.grid(row=r, column=c)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def on_click(self, r, c):
        if self.grid[r][c] == "1":
            # new island discovered
            self.island_count += 1
            self.label.config(text=f"Islands Found: {self.island_count}")

            # sink the entire island visually + internally
            self.sink_island(r, c)

        else:
            # clicking water or visited island = no effect
            pass

    def sink_island(self, r, c):
        # boundary checks
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            return
        
        if self.grid[r][c] != "1":
            return

        # mark as visited
        self.grid[r][c] = "0"
        self.buttons[r][c].config(bg="skyblue", text="0")

        # DFS - sink neighbors
        self.sink_island(r+1, c)
        self.sink_island(r-1, c)
        self.sink_island(r, c+1)
        self.sink_island(r, c-1)


def main():
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    root = tk.Tk()
    game = IslandGame(root, grid)
    root.mainloop()

if __name__ == "__main__":
    main()
