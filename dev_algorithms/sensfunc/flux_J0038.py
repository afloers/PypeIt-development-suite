import os
from flux_coadd_tell import flux_tell, stack_multinight

### sensfunction for NIRES
instrument = 'NIRES'

#basedir = '/d2/Feige/'
basedir = os.getenv('HOME')

std_path = os.path.join(basedir,'Dropbox/OBS_DATA/NIRES/SENSFUNC')
stdfile = 'spec1d_s190519_0059-GD153_NIRES_2019May19T083811.995.fits'

tell_method = 'qso'

sci_path = os.path.join(basedir,'Dropbox/OBS_DATA/NIRES/ut191111/Science')
z_qso = 7.1
fileroot = 'J0038-0653_NIRES'
flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso,
          tell_method=tell_method,
          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)