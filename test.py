import numpy as np
import catrxneng as cat

co2_fts = cat.reactions.CO2FTS(298)
rwgs = cat.reactions.RWGS(300)
fts = cat.reactions.FTS(300)
wgs = cat.reactions.WGS(500-273)
sab = cat.reactions.Sabatier(600)
print(sab.dH_rxn())
c2h4 = cat.species.C2H4(25)
print("done")