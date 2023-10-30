import tkinter

def submit_choices():
    selected_items = []
    for hobby, var in hobbies.items():
        if var.get():
            selected_items.append(hobby)
    text.delete('1.0', tkinter.END)
    selected_items_text = ', '.join(selected_items)
    text.insert(tkinter.END, "선택된 취미: {}\n".format(selected_items_text))

root = tkinter.Tk()
root.title("취미 선택 설문 조사")
root.geometry('400x200')

# 취미 목록
hobby = ["독서", "요리", "등산", "게임", "운동", "영화 감상", "여행", "사진 촬영"]

# 체크박스와 변수 저장을 위한 딕셔너리
hobbies = {}
for i in range(len(hobby)):
    hobbies[hobby[i]] = tkinter.BooleanVar()
    tkinter.Checkbutton(root, text=hobby[i], variable=hobbies[hobby[i]]).place(x=10, y=10+20*i)

button = tkinter.Button(root, text="선택 완료", command=submit_choices)
button.pack(side='bottom')

text = tkinter.Text(root, width=40, height=10)
text.place(x=100, y=20)

root.mainloop()
