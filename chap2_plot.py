import numpy as np
import matplotlib.pyplot as plt

# 2.2.1

x = np.linspace(-4, 4, 50, endpoint = True)
y = (4 * x**2) - 16

fig1 = plt.figure(num = 1, figsize = (5,5))
plt.plot(x,y)
plt.grid(True)
plt.title("x' = 4*x^2-16")
plt.xlabel('x')
plt.ylabel("x'")

#show the plot
fig1.show()

# 2.2.2
a = np.linspace(-2,2,50,endpoint=True)
b = 1-x**14

fig2 = plt.figure(num = 2, figsize = (5,5))
plt.plot(a,b)
plt.grid(True)
plt.title("x' = 1-x^14")
plt.xlabel('x')
plt.ylabel("x'")

fig2.show()

input()
