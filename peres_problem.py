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

ide_2q = np.kron(ide, ide)
x1 = np.kron(x, ide)
x2 = np.kron(ide, x)
y1 = np.kron(y, ide)
y2 = np.kron(ide, y)
x1y2 = np.kron(x, y)
y1x2 = np.kron(y, x)
x1x2y1y2 = np.kron(np.dot(x, y), np.dot(y, x))
pi_plus = 1/2*(ide_2q + x1)

# %%
""" We group them in appropriate sets of commuting 
observables that the user can choose to measure in one 
run of the experiment. """

sx = np.array([x1, x2])
sy = np.array([y1, y2])
s1 = np.array([x1y2, x1, y2])
s2 = np.array([y1x2, y1, x2])
s3 = np.array([x1y2, y1x2, x1x2y1y2])
set_obs = [sx, sy, s1, s2, s3]
sx_l = ['x1', 'x2']
sy_l = ['y1', 'y2']
s1_l = ['x1y2', 'x1', 'y2']
s2_l = ['y1x2', 'y1', 'x2']
s3_l = ['x1y2', 'y1x2', 'x1x2y1y2']
s_l = [sx_l, sy_l, s1_l, s2_l, s3_l]
set_l = ['sx', 'sy', 's1', 's2', 's3']

# %%
print("Ciao! In questa simulazione ti viene dato uno stato quantistico")
print("sul quale puoi effettuare delle misure. ")
print("Puntualizziamo che è possibile creare un sistema che si comporti ")
print("esattamente in questo modo in laboratorio. Devi immaginare quindi")
print("che tu stia effettuando un esperimento ed interpretare i risultati.")
print("Il sistema è costituito da due sottosistemi 1 e 2. Puoi ")
print("immaginare ogni sistema come un magnete (uno spin) del quale puoi")
print("misurare la magnetizzazione lungo la direzione x o y ad esempio.")
print("Ulteriori dettagli non ti vengono rivelati, ma sta a te scoprirli tramite" )
print("le misure appunto.")
print("Iniziamo! Puoi scegliere di misurare i seguenti gruppi di osservabili:")
print("sx = [x1, x2]")
print("sy = [y1, y2]")
print("s1 = [x1y2, x1, y2]")
print("s2 = [y1x2, y1, x2]")
print("s3 = [x1y2, y1x2]")
print("Una volta scelto l'insieme di grandezze, puoi scegliere la")
print("grandezza che vuoi misurare. Puoi misurare le grandezze all'interno")
print("di un insieme quante volte vuoi. Se vuoi cambiare insieme, puoi riavviare")
print("il programma da capo, iniziando un nuovo esperimento.")
print("Prendi nota delle tue osservazioni e conclusioni!")

# %%
k = False 
while k == False:
    s = input("Quale insieme vuoi misurare? sx/sy/s1/s2/s3 ")
    if set_l.count(s) > 0:
        k = True
    else:
        print("Scegli fra gli insiemi disponibili")

w = set_l.index(s)
s_meas = s_l[w]
rho = rho_singlet
# %%
print("Hai scelto di misurare il gruppo di grandezze")
print(s + ' = ' + str(s_meas))
print("")
k = False
while k == False:
    obs = input("Quale grandezza vuoi misurare? " + str(s_meas) + \
        " digita q per interrompere ")
    print("")
    if obs == 'q':
        print('Esperimento terminato')
        k = True
    elif s_meas.count(obs) > 0:
        w_obs = s_meas.index(obs)
        result = operations.pauli_measure(rho, set_obs[w][w_obs])
        print("Risultato misura " + str(obs) + ' = ' + str(result[0]))
        print("")
        rho = result[1]
    else:
        print("Scegli fra le grandezze disponibili")
        print("")


# %%
