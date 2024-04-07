from pygmo import *
ip = ipopt()
ip.set_numeric_option("tol",1E-9) # Change the relative convergence tolerance
ip.get_numeric_options() 
{'tol': 1e-09}
algo = algorithm(ip)
algo.set_verbosity(1)
prob = problem(luksan_vlcek1(20))
prob.c_tol = [1E-6] * 18 # Set constraints tolerance to 1E-6
pop = population(prob, 20)
pop = algo.evolve(pop) 