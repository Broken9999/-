import matplotlib.pyplot as plt

x = [2,3,7,16,17,14,17,12]
y = [2,3,7,16,17,14,17,12]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-')

for i, (xi, yi) in enumerate(zip(x, y)):
	plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
 
plt.plot(x1, y1, '-.')

plt.grid(True)


plt.show()

plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
plt.show()
