##
from pykep.trajopt import mga_1dsm
from pykep.planet import jpl_lp
from pykep import AU, DEG2RAD, MU_SUN, epoch
from pygmo import *
import pygmo as pg
import matplotlib.pyplot as plt

seq = [jpl_lp('earth'),jpl_lp('venus'),jpl_lp('earth')]
prob = mga_1dsm(seq=seq)

prob.tof= [0.7,3]
prob.vinf =[0.5,2.5]
prob.t0 = [epoch(5844),epoch(6209)]
prob.tof = [0.7,3]





prob = pg.problem(prob)
prob.c_tol = 1e-4


#ip = ipopt()
#ip.set_numeric_option("tol",1E-9)   #need gradient,but i don't know how to set
#algo = nsga2()                               #can't sole this type problem
algo = algorithm(nlopt('cobyla'))

algo.set_verbosity(1)
pop = pg.population(prob, 1)

# And optimize
pop = algo.evolve(pop)
print("Is feasible: ", prob.feasibility_f(pop.champion_f))
print("Final Mass at Mercury: ", -pop.champion_f[0], "Kg")


# Create the figure and axis
fig = plt.figure(figsize = (16,5))
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
prob.plot(pop.champion_x, axes = ax1)

ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax2.view_init(90, 0)
prob.plot(pop.champion_x, axes = ax2)

ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.view_init(0,0)
prob.plot(pop.champion_x, axes = ax3)