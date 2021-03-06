"""
Model M1a: Extrinsic apoptosis model with "embedded together" model of MOMP.
"""


from pysb import *
from earm import shared
from earm import lopez_modules
from earm import albeck_modules

Model()

# Declare monomers
albeck_modules.ligand_to_c8_monomers()
lopez_modules.momp_monomers()
albeck_modules.apaf1_to_parp_monomers()

# Generate the upstream and downstream sections
albeck_modules.rec_to_bid()
albeck_modules.pore_to_parp()

# The specific MOMP model to use
lopez_modules.embedded()

# Declare observables
shared.observables()

