import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
 
# Array für die Speicherung der Population
population = np.empty((52, 52))
 
# Anzahl Tage, die Simuliert werden sollen
tage = 30
 
# notwendig für die Darstellung der Grafik
fig = plt.figure()
cmap = plt.get_cmap('brg', 8)
mat = plt.imshow(population, cmap=cmap, interpolation='nearest', animated=True)
cax = plt.colorbar(mat, ticks=np.arange(0, 8))
plt.clim(0, 8)
plt.grid(True)
# Ende der Grafik Optionen
 
 
def update (tag):
  mat.set_data(population)
  plt.title("Tag: " + str(tag))
# initialer Zustand der Simulation
 
def setup():
  for i, j in np.ndindex(population.shape):
    population[i, j] = 0
  population[10,15]=1
  update(0)
  return mat
 
def get_zufall():
  zufall = random.randint(0, 3)
  return zufall
 
 
def ansteckung(x, y): 
  if population [x,y]==0:
    if  infektioes (x-1, y) > 0 or infektioes (x + 1, y) > 0 or infektioes (x, y - 1) > 0 or infektioes (x, y + 1) > 0:
      if get_zufall() == 0:
        population[x,y] = 1
  elif population [x,y] < 8:
    population [x, y] = population[x,y]+1 
       
def infektioes (x,y) :
  if population[x,y] > 1 and population[x,y] < 7:
    angesteckt=True
  else:
    angesteckt=False
  return angesteckt
 
 
# aktualisiert die Animation
def animate(t):
  for i, j in np.ndindex(population.shape):
    if 0 < i < 51 and 0 < j < 51:
      # Berechnung der Ansteckung
     ansteckung(i,j)
 
 
  # Aktualisierung der Darstellung mit den neuen Werten
  update(t)
  return mat
 
 
# Animiert die Darstellung
ani = animation.FuncAnimation(fig, animate, range(1, tage), repeat=False, interval=300, blit=False, init_func=setup)
writer = animation.PillowWriter(fps=5)
ani.save("./pandemie.gif", writer=writer)