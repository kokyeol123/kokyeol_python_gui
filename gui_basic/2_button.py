from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack() # pack 을 통해서 프로그램에 실제로 포함시킨다.

btn2 = Button(root, padx=5, pady=10, text="버튼2") 
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 패딩으로 버튼을 키우면 글자를 길게입력하면 버튼이 같이 길어지고 길이 넓이를 고정하면 글씨가 짤린다
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")

btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이클릭됨")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() # 창이 닫히지않도록