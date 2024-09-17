import matplotlib.pyplot as plt
import csv

data = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row[0])
    


target = list(map(float, data[0][1:len(data[0]) - 2].split(',')))
sample = list(map(float, data[1][1:len(data[1]) - 2].split(',')))

plt.figure(figsize=(10, 5))
plt.plot(target, label='Velocidade desejada')
plt.plot(sample, label='Velocidade obtida')
plt.legend()
plt.xlabel('Amostras')
plt.ylabel('Velocidade (rad/s)')
plt.title('Velocidade desejada e obtida')
plt.show()