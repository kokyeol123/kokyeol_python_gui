from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # Entry 는 한줄 Text는 여러줄
e.pack()
e.insert(0, "한 줄만 입력하세요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 라인 1, 0 : 컬럼 중에서 0번 인덱스
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지않도록