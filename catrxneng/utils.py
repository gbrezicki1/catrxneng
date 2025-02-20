import numpy as np


def dH(species):
    t = species.T_K / 1000
    params = species.thermo_params
    return (
        params["A"] * t
        + params["B"] * t**2 / 2
        + params["C"] * t**3 / 3
        + params["D"] * t**4 / 4
        - params["E"] / t
        + params["F"]
        - params["H"]
    )


def S(species):
    t = species.T_K / 1000
    params = species.thermo_params
    return (
        params["A"] *
          np.log(t)
        + params["B"] * t
        + params["C"] * t**2 / 2
        + params["D"] * t**3 / 3
        - params["E"] / (2 * t**2)
        + params["G"]
    )
