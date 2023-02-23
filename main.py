import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fq = 2000 #frequência de aquisição
dt = (1/fq) #intervalo de tempo
f0 = 100
N = int(10*fq/f0) #número de amostras
t = np.linspace(0, (N-1)*dt, N)
ft = fq/N #intervalo de frequencia
f = np.linspace(0, (N-1)*ft, N)
y = 1 * np.sin(2* np.pi * f0 * t) # amostra no domínio do tempo

X = np.fft.fft(y) # amostra no domínio da frquencia
X_mag = np.abs(X)/N

f_plot = f[0:int(N/2+1)]
X_plot = 2 * X_mag[0:int(N/2+1)]
X_plot[0] = X_plot[0]/2
fig , [ax1,ax2] = plt.subplots(nrows = 2 ,ncols = 1)
ax1.plot(t,y,'-.')
ax2.plot(f_plot,X_plot,'-.')
plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('ok')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
