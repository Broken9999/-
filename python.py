import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,3,7,16,17,14,17,12]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', label='Australia')

for i, (xi, yi) in enumerate(zip(x, y)):
	plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

x1 = [1,2,3,4,5,6,7,8,9]
y1 = [36,37,44,37,35,34,46,39,19]
 
plt.plot(x1, y1, marker='o', linestyle='-', label='USA')

for i, (xi, yi) in enumerate(zip(x1, y1)):
	plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

x2 = [1]
y2 = [1]
 
plt.plot(x2, y2, marker='o', linestyle='-', label='Vietnam')

for i, (xi, yi) in enumerate(zip(x1, y1)):
	plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')


plt.grid(True)

plt.legend()
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('Olympic')
plt.show()
