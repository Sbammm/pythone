

# Importazione delle librerie necessarie
import matplotlib.pyplot as plt  # Libreria per creare grafici in Python
import numpy as np  # Libreria per calcoli matematici e gestione di array

# Imposta uno stile predefinito per i grafici
plt.style.use('_mpl-gallery')  # Usa lo stile '_mpl-gallery' per il grafico

# Creazione dei dati per una doppia elica
n = 100  # Numero di punti per le due linee che rappresentano il grafico
theta = np.linspace(0, 2 * np.pi, n)  # Crea un array con 100 valori equispaziati tra 0 e 2π
x1 = np.cos(theta)  # Coordinate x del primo ramo della doppia elica
y1 = np.sin(theta)  # Coordinate y del primo ramo della doppia elica
z1 = np.linspace(0, 1, n)  # Coordinate z lineari che variano da 0 a 1 (altezza)
x2 = np.cos(theta + np.pi)  # Coordinate x del secondo ramo della doppia elica (sfasato di π)
y2 = np.sin(theta + np.pi)  # Coordinate y del secondo ramo della doppia elica (sfasato di π)
z2 = z1  # Coordinate z del secondo ramo (stessa altezza del primo ramo)

# Creazione del grafico
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})  # Crea una figura con un sottografico in 3D
ax.fill_between(x1, y1, z1, x2, y2, z2, alpha=0.5)  # Riempie l'area tra le due linee con trasparenza (alpha)
ax.plot(x1, y1, z1, linewidth=2, color='C0')  # Traccia il primo ramo della doppia elica in blu
ax.plot(x2, y2, z2, linewidth=2, color='C0')  # Traccia il secondo ramo della doppia elica in blu

# Rimuove le etichette dagli assi per rendere il grafico pulito
ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

# Mostra il grafico
plt.show()
