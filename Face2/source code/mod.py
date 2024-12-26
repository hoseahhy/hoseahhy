import tkinter as tk
from tkinter import messagebox
import pickle
import subprocess

# 加载先前保存的數據，如果存在的话
def load_data():
    try:
        with open('data.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return ["", "", "", ""]

# 保存數據到文件
def save_data(data):
    with open('data.pkl', 'wb') as f:
        pickle.dump(data, f)

def on_save():
    data = [entry1.get(), entry2.get(), entry3.get(), entry4.get()]
    save_data(data)
    window.destroy()  # 關閉當前視窗
    subprocess.run(["python", "Menu.py"])

def on_escape(event):
    window.destroy()  # 關閉當前視窗
    subprocess.run(["python", "Menu.py"])

# 建立主窗口
window = tk.Tk()
window.title("倉儲管理")

# 建立標籤和文本框
data = load_data()
for i in range(4):
    tk.Label(window, text=f"{i+1}.", width=5).grid(row=i, column=0)
    globals()[f'entry{i+1}'] = tk.Entry(window, width=20)
    globals()[f'entry{i+1}'].grid(row=i, column=1)
    globals()[f'entry{i+1}'].insert(0, data[i])

# 建立保存按钮
save_button = tk.Button(window, text="保存", command=on_save)
save_button.grid(row=4, columnspan=2)

# 绑定 Esc 键
window.bind('<Escape>', on_escape)

# 顯示視窗
window.mainloop()
