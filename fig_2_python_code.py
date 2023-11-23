import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
from scipy import constants


plt.rcParams['text.usetex'] = True


d = 0.0580583
s = np.linspace(0.0, 1.0, 100)
f = np.linspace(10, 0, 1000)
h = constants.hbar
k = constants.Boltzmann



def avgclockpf(s):
 return 0.5890 + 0.3004*np.exp(-s**2)

def avgclockpf_thermal(C,s):
 return 0.5552 + 0.03375*C + (-0.0001289 + 0.3005*C)*np.exp(-s**2)

def avgprobepf(d,f):
 return (1-2*d)*((1 + np.tanh(f))/2) + d**2*((1 - np.tanh(f))/2)

def appendpf(j,f):
 return (1/(2**j))*(1 + np.tanh(f))**j

fig, ay1 = plt.subplots()

color = 'tab:red'
ay1.plot(f, avgprobepf(d,f), label = '$\overline{\mathcal{F}}_{probe}$', linewidth = 2, color = color)
ay1.plot(f, appendpf(1,f), label = '$\overline{\mathcal{F}}_{appends}, \,\, J=1$', linewidth = 2, linestyle = 'dashed', color = color)
ay1.plot(f, appendpf(3,f), label = '$\overline{\mathcal{F}}_{appends}, \,\, J =3$', linewidth = 2, linestyle = 'dotted', color =color)
ay1.tick_params(axis='x', labelcolor=color)
ay1.invert_xaxis()
ay1.set_xlabel('$\\frac{ \\hbar \\omega }{k_B T}$', fontsize=16, color = color)
ay1.set_ylabel('$\mathcal{F}$', fontsize=16)

ay1.tick_params(axis='both', which='major', labelsize=16)
ay1.tick_params(axis='both', which='minor', labelsize=14)

ay2 = ay1.twiny()  # instantiate a second axes that shares the same y-axis

color = 'tab:blue'
ay2.set_xlabel('$\sigma$', fontsize=16, color=color)  # we already handled the x-label with ax1
ay2.plot(s, avgclockpf(s) , label = '$\overline{\mathcal{F}}_{clock}$', linewidth = 2)
ay2.plot(s, avgclockpf_thermal(0.75,s) , label = '$\overline{\mathcal{F}}_{clock}, \,\, C_{Max} = 0.75$', linewidth = 2, linestyle = 'dashed', color = color)
ay2.tick_params(axis='x', labelcolor=color)

ay2.tick_params(axis='both', which='major', labelsize=16)
ay2.tick_params(axis='both', which='minor', labelsize=14)

ay2.legend()
ay1.legend()


fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig("fid_compression_5.jpg",dpi=400)
plt.show()