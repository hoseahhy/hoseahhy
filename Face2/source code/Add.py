import cv2
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import subprocess


def ask_save_name():
    tk.Tk().withdraw()
    name = simpledialog.askstring("輸入名字", "請輸入圖片名字:")
    return name if name else "photo"  # 如果未輸入名字，使用預設名字 "photo"


def save_image(image):
    name = ask_save_name()
    save_path = f"C:\\Users\\hosea\\Desktop\\Face\\source code\\images\\{name}.jpg"
    cv2.imwrite(save_path, image)
    subprocess.run(["python", "Menu.py"])  # 啟動 Menu.py 程式


def show_and_ask(image):
    window = tk.Tk()
    window.title("圖片預覽")

    height, width, _ = image.shape
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image_rgb)
    imgtk = ImageTk.PhotoImage(img)

    label = tk.Label(window, image=imgtk)
    label.pack()

    def on_yes():
        window.destroy()
        save_image(image)
        # 由於 save_image 函數中已經包含了啟動 Menu.py 的程式碼，所以這裡不再需要

    def on_no():
        window.destroy()
        capture_image()

    yes_button = tk.Button(window, text="是", command=on_yes)
    no_button = tk.Button(window, text="否", command=on_no)
    yes_button.pack(side=tk.LEFT, padx=10, pady=10)
    no_button.pack(side=tk.RIGHT, padx=10, pady=10)

    window.mainloop()


def capture_image():
    cap = cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Press Space to Capture, Esc to Exit', frame)
        key = cv2.waitKey(1)
        if key == 27:  # Esc 鍵
            cap.release()
            cv2.destroyAllWindows()
            subprocess.run(["python", "Menu.py"])
            break
        elif key == 32:  # 空格鍵
            cap.release()
            cv2.destroyAllWindows()
            show_and_ask(frame)
            break


if __name__ == "__main__":
    capture_image()
