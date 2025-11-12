import tkinter as tk
import time

class SummaryRangesVisualizer:
    def __init__(self, root, nums):
        self.root = root
        self.nums = nums
        self.root.title("📊 Summary Ranges Visualizer")
        self.canvas = tk.Canvas(root, width=900, height=400, bg="#1e1e1e")
        self.canvas.pack(padx=10, pady=10)

        self.boxes = []
        self.box_size = 60
        self.offset_y = 100

        self.draw_array()
        self.root.after(1000, self.animate_ranges)  # starting animation

    def draw_array(self):
        """we draw initial array as boxes """
        x = 60
        for num in self.nums:
            box = self.canvas.create_rectangle(
                x, self.offset_y, x + self.box_size, self.offset_y + self.box_size,
                fill="#61dafb", outline="white", width=2
            )
            text = self.canvas.create_text(x + 30, self.offset_y + 30, text=str(num),
                                           font=("Helvetica", 16, "bold"), fill="black")
            self.boxes.append((box, text))
            x += self.box_size + 15
        self.root.update()

    def highlight_box(self, idx, color):
        """Highlight a box temporarily"""
        box, _ = self.boxes[idx]
        self.canvas.itemconfig(box, fill=color)
        self.root.update()
        time.sleep(0.5)

    def flash_text(self, message, color="#ffcc00"):
        """we displaya message temporarily"""
        msg = self.canvas.create_text(450, 50, text=message, fill=color,
                                      font=("Helvetica", 18, "bold"))
        self.root.update()
        time.sleep(1)
        self.canvas.delete(msg)

    def animate_ranges(self):
        """now animates the summary ranges logic"""
        if not self.nums:
            self.flash_text("⚠️ Empty array!")
            return

        result = []
        start = self.nums[0]
        x_pos = 100
        self.flash_text("🔍 Scanning the array...")

        for i in range(1, len(self.nums) + 1):
            if i < len(self.nums):
                self.highlight_box(i - 1, "#00e676")
            else:
                self.highlight_box(i - 1, "#00e676")

            if i == len(self.nums) or self.nums[i] != self.nums[i - 1] + 1:
                end = self.nums[i - 1]

                # Create a visual label for this range
                range_text = f"{start}" if start == end else f"{start}->{end}"
                self.flash_text(f"📦 Found range: {range_text}", color="#00ffff")

                self.canvas.create_text(
                    x_pos, 300, text=range_text,
                    font=("Helvetica", 18, "bold"), fill="#00ffff"
                )
                x_pos += 100
                result.append(range_text)

                if i < len(self.nums):
                    start = self.nums[i]

        self.flash_text("🏁 Done! All ranges formed!", color="#00ff00")
        print("Final Result:", result)


def main():
    nums = [0,1,2,4,5,7]
    root = tk.Tk()
    app = SummaryRangesVisualizer(root, nums)
    root.mainloop()


if __name__ == "__main__":
    main()
