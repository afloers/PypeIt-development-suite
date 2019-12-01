import os
from flux_coadd_tell import flux_tell, stack_multinight

### sensfunction for MOSFIRE
instrument = 'FLAMINGOS2'

#basedir = '/d2/Feige/'
basedir = os.getenv('HOME')

std_path = os.path.join(basedir,'Dropbox/OBS_DATA/FLAMINGOS/SENSFUNC')
stdfile = 'spec1d_S20191118S0196-HD27476_FLAMINGOS_2019Nov18T044652.500.fits'

tell_method = 'qso'
#tell_method = 'poly'


z_qso = 7.65
sci_path = os.path.join(basedir,'Dropbox/OBS_DATA/FLAMINGOS/ut191121/Science')
outroot = 'J0313-1806_FLAMINGOS'
spec1dfiles = ['spec1d_S20191121S0208-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191121S0209-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191121S0212-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191121S0213-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191121S0216-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191121S0217-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191121S0220-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191121S0221-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191121S0226-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191121S0227-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits']
objids = ['SPAT0978-SLIT0000-DET01','SPAT1089-SLIT0000-DET01','SPAT0978-SLIT0000-DET01','SPAT1089-SLIT0000-DET01',
          'SPAT0978-SLIT0000-DET01','SPAT1089-SLIT0000-DET01','SPAT0978-SLIT0000-DET01','SPAT1088-SLIT0000-DET01',
          'SPAT1088-SLIT0000-DET01','SPAT0978-SLIT0000-DET01']
flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, spec1dfiles=spec1dfiles, objids=objids,
          outroot=outroot, z_qso=z_qso, tell_method=tell_method, star_type='A0V', star_mag=8.73,
          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)