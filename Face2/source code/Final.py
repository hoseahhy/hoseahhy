import cv2
from simple_facerec import SimpleFacerec
import pickle
import tkinter as tk

# Encode faces from a folder
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("C:\\Users\\hosea\\Desktop\\Face\\source code\\images")

# Load Camera
cap = cv2.VideoCapture(1)

# Load names data
def load_names():
    try:
        with open('data.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return ["", "", "", ""]

names_data = load_names()

# Cargo Window
class CargoWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cargo Status")

        self.cargo_status = ["待取貨"] * 4  # Initial status
        self.labels = []

        for i in range(4):
            var = tk.StringVar(value=self.cargo_status[i])
            label = tk.Label(self.window, textvariable=var, width=10, height=2, borderwidth=2, relief="solid")
            label.grid(row=0, column=i)
            self.labels.append(var)

        self.window.after(10, self.update)  # Schedule the update method to run after 10 ms

    def update_status(self, index):
        if 0 < index <= len(self.cargo_status):
            self.cargo_status[index - 1] = "取貨完成"
            self.labels[index - 1].set("取貨完成")

    def update(self):  # New method to handle face recognition and updating cargo status
        global cap

        ret, frame = cap.read()
        name_index = 0

        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            try:
                name_index = names_data.index(name) + 1
            except ValueError:
                name_index = 0

            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        cv2.putText(frame, str(name_index), (frame.shape[1] - 50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)

        if name_index in [1, 2, 3, 4]:
            self.update_status(name_index)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            cap.release()
            cv2.destroyAllWindows()
            self.window.quit()  # Close the tkinter window
        else:
            self.window.after(10, self.update)  # Schedule the next update

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    cargo_window = CargoWindow()
    cargo_window.run()
