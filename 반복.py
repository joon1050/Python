import pyautogui
import time
from tkinter import *

root = Tk()
root.title("카톡 보내기")
root.geometry("300x150+790+400") # 가로 * 세로

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

pos_text = (1216, 656)
pos_send = (1502, 731)

tx, ty = pos_text
sx, sy = pos_send

l = Label(root, text="%영어로 적고 한국어로 바꿔야합니다%")
l.pack()

e = Entry(root, width=30)
e.pack()
e.insert(0, "뭐라 보낼지 적으세요")

r = Entry(root, width=30)
r.pack()
r.insert(0, "갯수를 적으세요")


def btncmd():
    var = e.get()
    var2 = r.get()

    print('입력하신 문자 : {}'.format(var))
    print('입력하신 숫자 : {}'.format(var2))
    print("----------------------------")

    for i in range(int(var2)):
        pyautogui.moveTo(tx, ty, duration=0)
        pyautogui.click()
        pyautogui.write(var)
        time.sleep(0.1)
        pyautogui.typewrite(["enter"])
        print("{}번 전송 완료".format(i))

    l.config(text="완료되었습니다")
    
    time.sleep(1)

    root.quit()

btn = Button(root, text="보내기", command=btncmd)
btn.pack()

root.mainloop()