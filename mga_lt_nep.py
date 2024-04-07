# Imports
import pykep as pk
import pygmo as pg
from pygmo import nsga2
import numpy as np
from pykep.examples import add_gradient

# Plotting imports
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
udp = pk.trajopt.mga_lt_nep(
     seq = [pk.planet.jpl_lp('earth'), pk.planet.jpl_lp('venus'), pk.planet.jpl_lp('venus')],
     n_seg = [5, 20],
     t0 = [3000, 4000], # This is in mjd2000
     tof = [[100, 1000], [200, 2000]], # This is in days
     vinf_dep = 3., # This is in km/s
     vinf_arr = 2., # This is in km/s
     mass = [1000., 2000.0],
     Tmax = 0.5,
     Isp = 3500.0,
     fb_rel_vel = 6., # This is in km/s
     multi_objective = False,
     high_fidelity = False
    
)

#print(prob)


prob = pg.problem(udp)
prob.c_tol = 1e-4


#ip = ipopt()
#ip.set_numeric_option("tol",1E-9)   #need gradient
#algo = nsga2()                               #can't sole this type problem
algo = algorithm(nlopt('cobyla'))

algo.set_verbosity(3)
pop = pg.population(prob, 3)

# And optimize
pop = algo.evolve(pop)
print("Is feasible: ", prob.feasibility_f(pop.champion_f))
print("Final Mass at Mercury: ", -pop.champion_f[0], "Kg")
mpl.rcParams['legend.fontsize'] = 10

# Create the figure and axis
fig = plt.figure(figsize = (16,5))
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
udp.plot(pop.champion_x, axes = ax1)

ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax2.view_init(90, 0)
udp.plot(pop.champion_x, axes = ax2)

ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.view_init(0,0)
udp.plot(pop.champion_x, axes = ax3)