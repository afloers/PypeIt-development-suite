import os
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

#from pypeit.core import coadd1d
#from coadd1d_old import *
#from pypeit.core.coadd1d import *
from pypeit.core import load, save
from pypeit.core import coadd1d

## GMOS test
datapath = os.path.join(os.getenv('HOME'), 'Dropbox/PypeIt_Redux/GMOS/R400_Flux/')
fnames = [datapath + 'spec1d_flux_S20180903S0136-J0252-0503_GMOS-S_1864May27T160716.387.fits', \
          datapath + 'spec1d_flux_S20180903S0137-J0252-0503_GMOS-S_1864May27T160719.968.fits', \
          datapath + 'spec1d_flux_S20180903S0138-J0252-0503_GMOS-S_1864May27T160723.353.fits', \
          datapath + 'spec1d_flux_S20180903S0141-J0252-0503_GMOS-S_1864May27T160727.033.fits', \
          datapath + 'spec1d_flux_S20180903S0142-J0252-0503_GMOS-S_1864May27T160730.419.fits', \
          datapath + 'spec1d_flux_S20181015S0140-J0252-0503_GMOS-S_1864May27T185252.770.fits']
objids = ['SPAT1073-SLIT0001-DET03', 'SPAT1167-SLIT0001-DET03', 'SPAT1071-SLIT0001-DET03', 'SPAT1072-SLIT0001-DET03',
         'SPAT1166-SLIT0001-DET03', 'SPAT1073-SLIT0001-DET03']

# parameters for load_1dspec_to_array
ex_value = 'OPT'
flux_value = True

#wave_stack, flux_stack, ivar_stack, mask_stack = coadd1d.multi_combspec(fnames, objids, debug=False)


