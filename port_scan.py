import serial.tools.list_ports

def find_serial_ports():
    ports = serial.tools.list_ports.comports()
    serial_ports = []
    for port, desc, hwid in sorted(ports):
        print(port,desc,hwid)
        if 'COM' in port:
            serial_ports.append(port)
    
    
    
    return serial_ports
def scan():
    available_ports = find_serial_ports()
    if available_ports:
        print("Available serial ports:")
        for port in available_ports:
            print("--- "+str(port))
    else:
        print("No serial ports found.")
