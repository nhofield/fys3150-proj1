import numpy as np
import os
import time
import matplotlib.pyplot as plt

t1 = time.time()
N = 5
eps_relative = np.zeros(N)
number_N = np.zeros(N)
u_exact = lambda x: 1. - (1. - np.exp(-10.))*x - np.exp(-10.*x)
filename = "proj1aRun.dat"

for i in range(N):
    n = 10**(i+1)
    run = os.system("g++ project1.cpp -o project1 && ./project1 %d && rm project1" % n)
    x1, y1 = np.loadtxt(filename, unpack=True)
    eps_relative[i] = np.linalg.norm(u_exact(x1) - y1)/np.linalg.norm(u_exact(x1))
    number_N[i] = n


print number_N
F = 14
plt.figure(figsize=(10,8))
plt.xlabel(r"$log_{10}(n)$", fontsize=F)
plt.ylabel(r"$log_{10}\epsilon_{relative}$", fontsize=F)
plt.plot(np.log10(number_N), np.log10(eps_relative), label=r"$log_{10}\epsilon_{relative}(n)$")
plt.grid(True)
t2 = time.time()
print t2-t1, "seconds"
plt.show()