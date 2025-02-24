import numpy as np
import catrxneng as cat

w = 2 # g
P = 20 # bara
whsv = {"nmlm/gcat": 100}
mol_gas_vol = cat.constants.mol_gas_vol
whsv["mmol/min/gcat"] = whsv["nmlm/gcat"] / mol_gas_vol["nL/mol"]
labels = ["co2", "h2", "co", "h2o", "inert"]
y0 = np.array([0.2, 0.6, 0, 0, 0.2])
k1f = 0.02
k1r = 31 * k1f
r = np.array([
    lambda p: k1r*p[2]*p[3] - k1f*p[0]*p[1],
    lambda p: k1r*p[2]*p[3] - k1f*p[0]*p[1],
    lambda p: k1f*p[0]*p[1] - k1r*p[2]*p[3],
    lambda p: k1f*p[0]*p[1] - k1r*p[2]*p[3],
    lambda p: 0,
])

pfr = cat.reactors.PFR(w=w,P=P,whsv=whsv["mmol/min/gcat"],y0=y0,r=r)
rwgs = cat.reactions.RWGS(temp_C=320)
Xeq = rwgs.Xeq(y0*P)
pfr.plot_conv_vs_w("CO2 conv.",Xeq)