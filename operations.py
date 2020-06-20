"""
The file contains classes and functions for manipulations
of quantum states
"""

import numpy as np

def pauli_measure(rho, pauli):
    """ The density matrix rho and the pauli operator
    pauli must be numpy arrays """

    n = 2
    ide = np.identity(2**n, dtype=complex)
    pi_plus = 1/2*(ide + pauli) #projector on +1 eigenspace 
    pi_minus = 1/2*(ide - pauli) #projector on -1 eigenspace 
    p = np.trace(pi_plus.dot(rho)) #probability of +1 measurement
    x = np.random.random()
    if x < p:
        rho_plus = pi_plus.dot(rho.dot(pi_plus))
        rho_plus = rho_plus/np.trace(rho_plus)
        return 1, rho_plus
    else:
        rho_minus = pi_minus.dot(rho.dot(pi_minus))
        rho_minus = rho_minus/np.trace(rho_minus)
        return -1, rho_minus
