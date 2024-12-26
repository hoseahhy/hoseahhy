import serial

COM_PORT = 'COM3' 
BAUD_RATES = 9600
arduinoSerial = serial.Serial(COM_PORT, BAUD_RATES)

try:
    while True:
        choice = input('109')
        if choice == '1':
            print('1')
            arduinoSerial.write(b'1')
        elif choice == '0':
            print('0')
            arduinoSerial.write(b'0')
        elif choice == '9':
            print('close')
            arduinoSerial.close()
            exit()
        else:
            print('指令錯誤')

except KeyboardInterrupt:
    arduinoSerial.close()
    print('關閉程式')