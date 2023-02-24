import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#data frame original
filename = 'teste.txt'
df = pd.read_csv(filename, sep = '\t') # data frame com dados do acelerômetro

# delta tempo
df['dt'] = df['t'] - df['t'].shift()
df['dt'][0] = df['dt'][1]

# Velocidade
df['v'] = 0
df['v'] = df['v'] + df['v'].shift() + df['A']*df['dt']
df['v'][0] = 0

# Deslocamento
df['x'] = 0
df['x'] = df['x'] + df['x'].shift() + df['v']*df['dt']
df['x'][0] = 0

# Determina a frquência de aquisição
df2 = df.copy()
df2.drop(df2[(df2['t'] < 5.5) ].index,inplace = True)
df2.drop(df2[(df2['t'] > 6.5) ].index,inplace = True)
F = len(df2)   # frquência de aquisição

# Delimita o intervalo de da excitação
df.drop(df[(df['t'] < 5.5025) ].index,inplace = True)
df.drop(df[(df['t'] > 5.54) ].index,inplace = True)
df['t'] = df['t'] - df['t'].min() # corrige tempo inicial

N = len(df) # Número de amostras no intervalo
fstep = F/N # step frquencia
f = np.linspace(0, (N-1)*fstep, N) # vetor frequência
#f_plot = f[0:int(N/2+1)]

#variáveis
t = df['t'] #Tempo
A = df['A'] #aceleração
V = df['v'] #velocidade
x = df['x'] #posição

#diagrama de Nyquist
X = np.fft.fft(x)
X_mag = np.abs(X) / N

f_plot = f[0:int(N/2+1)]
X_mag_plot = 2 * X_mag[0:int(N/2+1)]
X_mag_plot[0] = 0


'''def func(S, Y, a, b, m, c, k):
    return (a*S + b)/(m*S**2 + c*S + k)

popt, pcov = curve_fit(func, df['t'], df['x'])

print(popt)'''


print(r'Frequência de aquisição: {} hz'.format(F))
print(r'Número de Amostras no Intervalo: {} '.format(N))
print(df)


# Figura
fig , [ax1,ax2,ax3] = plt.subplots(nrows = 3,ncols = 1)
ax1.plot(t,A,'k-')
ax1.set_xlabel('time [s]')
ax1.set_ylabel('A [m/s²]')

ax2.plot(t,V,'k-')
ax2.set_xlabel('time [s]')
ax2.set_ylabel('V [mm/s]')

ax3.plot(t,x,'k-')
#ax3.plot(t,func(df['t'],*popt),'b--')
ax3.set_xlabel('time [s]')
ax3.set_ylabel('X [m]')
'''
plt.tight_layout()
plt.show()'''

fig2, [ax21,ax22] = plt.subplots(nrows = 2,ncols = 1)
ax21.plot(t,x,'k-')
ax21.set_xlabel('time [s]')
ax21.set_ylabel('X [m]')

ax22.plot(f_plot,X_mag_plot,'k-')
ax22.set_xlabel('f [Hz]')
ax22.set_ylabel('X [db(A)]')

plt.tight_layout()
plt.show()