import serial


def leer_balanza(puerto):
    puerto_balanza = '/dev/ttyUSB0' 
    ser = serial.Serial(puerto, 9600, timeout=1)
    ser.flush()
    
    if ser.in_waiting > 0:
        linea = ser.readline().decode('utf-8').rstrip()
        return linea

if __name__ == '__main__':
    puerto_balanza = '/dev/ttyUSB0'  # Reemplaza esto con el nombre de tu puerto serial
    leer_balanza(puerto_balanza)