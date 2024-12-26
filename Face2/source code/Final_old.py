
import cv2
from simple_facerec import SimpleFacerec
import serial
"""
OM_PORT = 'COM7' 
BAUD_RATES = 9600
arduinoSerial = serial.Serial(COM_PORT, BAUD_RATES)
"""

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(1)


while True:
    ret, frame = cap.read()

    # s = input
    # if s == 0:
    #     arduinoSerial.write(b'0')

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    if len(face_names) != 0:
        print(face_names[0])
        """
        if face_names[0] == "Kevin":
            print('貨櫃1開')
            arduinoSerial.write('A')
        
        elif face_names[0] == "Peter":
            print('貨櫃2開')
            arduinoSerial.write('S')
            
        elif face_names[0] == "Chan":
            print('貨櫃3開')
            arduinoSerial.write('D')
            
        elif face_names[0] == "David":
            print('貨櫃4開')
            arduinoSerial.write('F')
        """
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
