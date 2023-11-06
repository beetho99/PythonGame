import tkinter

key =''
pic_index = 1

def key_down(e):
    global key
    key = e.keysym
def key_up():
    global key
    key = ''
def main_proc():
    global pic_index, img
    label['text'] = 'Picture Number : ' + str(pic_index)
    img = tkinter.PhotoImage(file='photo'+str(pic_index)+'.png')
    canvas.delete('PHOTO')
    canvas.create_image(400, 300, image=img, tag='PHOTO')
    if key == 'Up' or key == 'Right':
        pic_index += 1
        if pic_index == 5:
            pic_index = 1
    if key == 'Down' or key == 'Left':
        pic_index -=  1
        if pic_index == 0:
            pic_index = 4
    root.after(1000, main_proc)

root = tkinter.Tk()
root.title('디지털 액자')
root.geometry('800x600')
label = tkinter.Label(font=('Times New Roamn', 14))
label.pack(side='bottom')
canvas = tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()
img = tkinter.PhotoImage(file='photo'+str(pic_index)+'.png')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
main_proc()
root.mainloop()