import serial
import csv
import time

porta = 'COM3'
baudrate = 115200
duration = 5

target = []
sample = []


ser = serial.Serial(porta, baudrate)
time.sleep(2)  # Aguarde a inicialização do Arduino
start_time = time.time()

while time.time() - start_time < duration:
    line = str(ser.readline().decode('utf-8'))
    data = line.split()
    target.append(float(data[0]))
    sample.append(float(data[1]))

ser.close()



with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([target])
    writer.writerow([sample])

print('done')


