"""
The script is based on one of the problem analyzed in the classic
Mermin's paper "Simple Unified Form for the Major No-Hidden
Variables Theorems" Phys. Rev. Lett., 65 (1990), which is actually
originally due to Peres in Phys. Lett. A, 151 (1990). 
"""

#%%
import numpy as np

#%% 
""" We define Pauli operators and introduce the singlet state """
singlet = np.transpose(1/np.sqrt(2)*np.array([[0, 1, -1, 0]]))
ide = np.identity(2, dtype=complex)
x = np.array([[0, 1], [1, 0]], dtype=complex)
y = np.array([[0, -1j], [1j, 0]], dtype=complex)
z = np.array([[1, 0], [0, -1]], dtype=complex)

# %%
""" Relevant operators in Peres' problem """
x1 = np.kron(x, ide)
x2 = np.kron(ide, x)
y1 = np.kron(y, ide)
y2 = np.kron(ide, y)
x1y2 = np.kron(x, y)
y1x2 = np.kron(y, x)


# %%
