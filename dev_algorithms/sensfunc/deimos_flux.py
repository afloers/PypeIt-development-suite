import numpy as np
from dev_flux_tell import flux_tell

#### sensfunction for DEIMOS
instrument = 'DEIMOS'

#### Generate SENSFUNC
## 830G centered at 8100A
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/Feige110/Science'
stdfiles = ['spec1d_d0526_0134-Feige110_DEIMOS_2017May26T145952.051.fits']
for ii in range(len(stdfiles)):
    stdfile = stdfiles[ii]
    flux_tell(sci_path, stdfile, instrument=instrument, do_sens=True, do_flux=False, do_stack=False, do_tell=False,
              disp=True, debug=True)

