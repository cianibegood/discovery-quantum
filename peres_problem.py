"""
The script is based on one of the problem analyzed in the classic
Mermin's paper "Simple Unified Form for the Major No-Hidden
Variables Theorems" Phys. Rev. Lett., 65 (1990), which is actually
originally due to Peres in Phys. Lett. A, 151 (1990). 
"""

#%%
import numpy as np
import operations
import importlib

#%% 
""" We define Pauli operators and introduce the singlet state """

ket_singlet = np.transpose(1/np.sqrt(2)*np.array([[0, 1, -1, 0]]))
#rank-1 projector of a singlet (density matrix)
rho_singlet = ket_singlet.dot(ket_singlet.T.conj()) 
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
""" We group them in appropriate sets of commuting 
observables that the user can choose to measure in one 
run of the experiment. """

sx = np.array([x1, x2])
sy = np.array([y1, y2])
s1 = np.array([x1y2, x1, y2])
s2 = np.array([y1x2, y1, x2])
s3 = np.array([x1y2, y1x2])

# %%
pippo = operations.pauli_measure(rho_singlet, x1)

# %%
