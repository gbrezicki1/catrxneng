from .utils import dH, S


class CO:
    def __init__(self, T_C):
        self.T_C = T_C
        self.T_K = T_C + 273
        self.Hf_298 = -110530  # J/mol
        self.S_298 = 197.66  # J/mol
        self.thermo_params = {
            "A": 25.56759,
            "B": 6.096130,
            "C": 4.054656,
            "D": -2.671301,
            "E": 0.131021,
            "F": -118.0089,
            "G": 227.3665,
            "H": -110.5271,
        }

    def H(self):
        return self.Hf_298 + dH(self)

    def S(self):
        return S(self)
