import tkinter
root = tkinter.Tk()
root.title('첫 번째 캔버스')
canvas = tkinter.Canvas(root, width=400, height=600, bg='skyblue')
canvas.pack()
gazou = tkinter.PhotoImage(file='hyunju.png')
canvas.create_image(200, 300, image=gazou)
root.mainloop()