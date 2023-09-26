import subprocess
import sys
import tkinter as tk
def button1_click():
    window = tk.Tk()
    window.title("모드를 선택하시오")
    window.geometry("300x300")
    button3 = tk.Button(window, text="전문가용", width=15, height=2, command=button3_click, bg="red", fg="white")
    button3.pack(side=tk.LEFT, padx=20)
    button4 = tk.Button(window, text="초보자용", width=15, height=2, command=button3_click, bg="blue", fg="white")
    button4.pack(side=tk.RIGHT, padx=20)


def button2_click():
    subprocess.run(args=[sys.executable, 'learning.py'])

def button3_click():
    subprocess.run(args=[sys.executable, 'translater(fast).py'])

def button4_click():
    subprocess.run(args=[sys.executable, 'translater.py'])
window = tk.Tk()
window.title("둘 중 하나를 고르시오")
window.geometry("300x300")

# 버튼 1

button1 = tk.Button(window, text="번역기", width=15, height=2, command=button1_click)
button1.pack(side=tk.LEFT, padx=20)

# 버튼 2
button2 = tk.Button(window, text="학습기", width=15, height=2, command=button2_click)
button2.pack(side=tk.RIGHT, padx=20)

window.mainloop()