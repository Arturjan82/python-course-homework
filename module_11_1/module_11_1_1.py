# -- coding: utf8 --
import matplotlib.pyplot as plt
import numpy as np

x = [0, 2, 8, 9]
y = [0, 5, 7, 14]
plt.plot(x,y)
plt.show()

x = np.array([0,2,3,4])
y = np.array([0,2,1,5])

plt.plot(x,y)
plt.xlabel('Ось X') # Название ось X
plt.ylabel('Ось Y')  # Название ось Y
plt.title('Заголовок', fontsize = 20)
plt.show()