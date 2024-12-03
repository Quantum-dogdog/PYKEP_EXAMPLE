def run(solver="ipopt"):
    import pygmo as pg
    from pykep import epoch
    from pykep.planet import jpl_lp
    from pykep.trajopt import mga_1dsm
    from pykep.examples import add_gradient, algo_factory
    # We define an Earth-Venus-Earth problem (single-objective)
    cai = [9.59683826e+03,6.72324970e-01,5.66690265e-01,5.67276964e+02,2.30498730e-01,2.66988197e+02,4.26696327e+00,2.93015436e+00,2.40608607e-01,2.98497829e+02,3.01019636e+00,6.28338162e+00,2.21726682e-01,3.63974069e+02,-1.47686413e+00,1.14288266e+00,1.38317073e-01,1.09575000e+03]
    #initial guess


    seq = [jpl_lp('earth'), jpl_lp('venus'), jpl_lp('earth'), jpl_lp('earth'), jpl_lp('jupiter')]
    algo = algo_factory(solver)
    udp = add_gradient(mga_1dsm(
        seq=seq,
        t0=[epoch(9132), epoch(11000)],           #2025-01-01是9132
        tof=[
            [0.5 * 365.25, 1.3 * 365.25],
            [0.1 * 365.25, 1.3 * 365.25],
            [0.5 * 365.25, 1.3 * 365.25],
            [0.5 * 365.25, 3 * 365.25],
            ],
        vinf = [0.5, 2.5],
        add_vinf_dep=True,
        add_vinf_arr=True,
        multi_objective=False
    ),with_grad = True)

    prob = pg.problem(udp)
    

    # 3 - Population (i.e. initial guess)
    pop = pg.population(prob)
    pop.push_back(cai)
    # 4 - Solve the problem (evolve)
    pop = algo.evolve(pop)
    print(
        "Running a ipopt")
    
    # 在调用 udp.udp_inner.pretty 之前
    print("pop.champion_x:", pop.champion_x)
    if len(pop.champion_x) == 0:
       print("No solution found. Check the optimization setup.")
    else:
       udp.udp_inner.pretty(pop.champion_x)
       udp.udp_inner.plot(pop.champion_x)
      
    
    
    
if __name__ == "__main__":
    run()



