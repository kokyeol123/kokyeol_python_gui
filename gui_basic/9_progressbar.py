import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def closer(event):
    root.destroy()

root.bind("<Escape>", closer)

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate 왕복으로 계속 움직임
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # determinate 100프로까지 차는 느낌
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # 매번 바뀔 때 반영되게한다. 안쓰면 0에서 100으로 한번에 찬다.
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()