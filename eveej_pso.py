def run():
    import pygmo as pg
    from pykep import epoch
    from pykep.planet import jpl_lp
    from pykep.trajopt import mga_1dsm

    # We define an Earth-Venus-Earth problem (single-objective)
    seq = [jpl_lp('earth'), jpl_lp('venus'), jpl_lp('earth'), jpl_lp('earth'), jpl_lp('jupiter')]
    udp = mga_1dsm(
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
    )

    pg.problem(udp)
    # We solve it!!
    uda = pg.pso(gen=200)

    uda = pg.algorithm(uda)
    
    pop = pg.population(udp,2000)
    
    print(
        "Running a 粒子群优化")
    pop = uda.evolve(pop)
    
    
    print("Done!! Solutions found are: ", pop.champion_f)
    udp.pretty(pop.champion_x)
    udp.plot(pop.champion_x)
if __name__ == "__main__":
    run()



