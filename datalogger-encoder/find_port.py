import serial
import serial.tools.list_ports
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def find_first_available_com_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        return port.device
    return None

if is_admin():
    first_com_port = find_first_available_com_port()
    if first_com_port:
        try:
            ser = serial.Serial(first_com_port, 9600)
            print(f"Conectado com sucesso na porta {first_com_port}!")
        except serial.SerialException as e:
            print(f"Erro ao abrir a porta serial {first_com_port}: {e}")
    else:
        print("Nenhuma porta COM disponível foi encontrada.")
else:
    print("Por favor, execute como administrador.")