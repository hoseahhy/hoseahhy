import tkinter as tk
import subprocess

# 建立主視窗
window = tk.Tk()
window.title("程式管理")


def run_script(script_name):
    window.destroy()  # 關閉當前視窗
    subprocess.run(["python", script_name])


def run_script1():
    run_script("Final.py")


def run_script2():
    run_script("Add.py")


def run_script3():
    run_script("mod.py")


# 建立按鈕
button1 = tk.Button(window, text="取貨", command=run_script1, width=10, height=2)
button2 = tk.Button(window, text="新增", command=run_script2, width=10, height=2)
button3 = tk.Button(window, text="管理", command=run_script3, width=10, height=2)

# 排列按鈕
button1.pack(side=tk.LEFT, padx=10, pady=10)
button2.pack(side=tk.LEFT, padx=10, pady=10)
button3.pack(side=tk.LEFT, padx=10, pady=10)

# 顯示視窗
window.mainloop()
