import tkinter as tk

def draw_chessboard(canvas, size=60):
    colors = ["white", "black"]
    for row in range(8):
        for col in range(8):
            x1 = col * size
            y1 = row * size
            x2 = x1 + size
            y2 = y1 + size
            color = colors[(row + col) % 2]
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

# Pencere oluştur
root = tk.Tk()
root.title("Satranç Tahtası")

# Tuval (canvas) oluştur
board_size = 8 * 60  # 8 kare, her biri 60 piksel
canvas = tk.Canvas(root, width=board_size, height=board_size)
canvas.pack()

# Tahtayı çiz
draw_chessboard(canvas)

# Pencereyi çalıştır
root.mainloop()
