import serial

def leer_datos_pesa( baud_rate=9600, bytes_size=8, timeout=1):
    try:
        puerto_serial = "COM3"
        # Configurar la conexión serial
        conexion = serial.Serial(port=puerto_serial, baudrate=baud_rate, bytesize=bytes_size, timeout=timeout)
        print("Conexión establecida con éxito a", puerto_serial)

        # Bucle infinito para leer continuamente datos de la pesa
        while True:
            datos = conexion.readline().decode().strip()
            print(datos)
            print("Conexión holandauhjyty")
            if datos:
                return datos  # Devolver los datos leídos

    except serial.SerialException as e:
        print("Error al conectar con la pesa:", e)

