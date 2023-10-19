import tkinter as tk

index = 0
image_files = ["singapore1.png", "singapore2.png", "singapore3.png"]

def load_image():
    global photo
    photo = tk.PhotoImage(file=image_files[index])
    canvas.create_image(400, 300, image=photo)

def prev_image():
    global index
    index -= 1 
    if index < 0:
        index = len(image_files) - 1
    load_image()

def next_image():
    global index
    index += 1
    if index >= len(image_files):
        index = 0
    load_image()

root = tk.Tk()
root.title("이미지 플레이어")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

load_image()

btn_prev = tk.Button(root, text="이전", command=prev_image)
btn_prev.place(x=50, y=550)
btn_next = tk.Button(root, text="다음", command=next_image)
btn_next.place(x=100, y=550)

root.mainloop()
