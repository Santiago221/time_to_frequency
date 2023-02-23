import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lvm_read as lvm

filename = 'teste.txt'
df = pd.read_csv(filename, sep = '\t') # data frame com dados do acelerômetro


df2 = df.copy()
df2.drop(df2[(df2['t'] < 5.5) ].index,inplace = True)
df2.drop(df2[(df2['t'] > 6.5) ].index,inplace = True)
F = len(df2)   # frquência de aquisição

df.drop(df[(df['t'] < 5.5) ].index,inplace = True)
df.drop(df[(df['t'] > 5.54) ].index,inplace = True)
df['t'] = df['t'] - df['t'].min()
N = len(df) # Número de amostras no intervalo
fstep = F/N # step frquencia
f = np.linspace(0, (N-1)*fstep, N) # vetor frequência
f_plot = f[0:int(N/2+1)]

t = df['t']
Y = df['a']
Y_freq = np.fft.fft(Y) # amostra no domínio da frquencia
Y_freq_mag = abs(Y_freq)/N
Y_freq_mag_plot = 2 * Y_freq_mag[0:int(N/2+1)]
Y_freq_mag_plot[0] = Y_freq_mag_plot[0]/2
df_f = pd.DataFrame(np.array([f_plot,Y_freq_mag_plot]).T,columns = ['f','Y']) #dataframe com dados de frequência
fn = df_f['Y'].max()

M = 200 # massa kg
K = M*(fn*2*np.pi) **2

print(r'Frequência de aquisição: {} hz'.format(F))
print(r'Número de Amostras no Intervalo: {} '.format(N))
print(r'Frequência Natural: {} hz'.format(fn))
print(r'Massa: {} kg'.format(M))
print(r'Rigidez: {} N/m'.format(K))
# Figura
fig , [ax1,ax2] = plt.subplots(nrows = 2 ,ncols = 1)
ax1.plot(t,Y,'-.')
ax1.set_xlabel('time [s]')
ax1.set_ylabel('A [m/s²]')

ax2.plot(f_plot,Y_freq_mag_plot,'--')
ax2.set_ylabel('dB [A]')
ax2.set_xlabel('f [hz]')
plt.tight_layout()
plt.show()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('ok')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
