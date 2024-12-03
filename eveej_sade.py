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
    uda = pg.sade(gen=200)
    archi = pg.archipelago(algo=uda, prob=udp, n=10, pop_size=20)
    print(
        "Running a Self-Adaptive Differential Evolution Algorithm .... on 10 parallel islands")
    archi.evolve(10)
    archi.wait()
    sols = archi.get_champions_f()            #fitness，就是总的deltaV
    idx = sols.index(min(sols))
    print("Done!! Solutions found are: ", archi.get_champions_f())
    udp.pretty(archi.get_champions_x()[idx])
    udp.plot(archi.get_champions_x()[idx])
if __name__ == "__main__":
    run()
