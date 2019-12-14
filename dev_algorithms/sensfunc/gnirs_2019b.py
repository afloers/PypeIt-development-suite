import numpy as np
from flux_coadd_tell import flux_tell, stack_multinight

instrument = 'GNIRS'


std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/SENSFUNC/'
stdfile = 'spec1d_cN20161014S0481-GD71_GNIRS_2016Oct14T152107.457.fits'

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190908_Tdwarf/Science/'
fileroot = 'J0203-0106_GNIRS'
z_qso = 7.0
tell_method = 'poly'
## Wavelength have problem in the redside, thus I cut out at 24800.0
#flux_tell(sci_path, stdfile, std_path=std_path,instrument=instrument, fileroot=fileroot, z_qso=z_qso,
#          tell_method=tell_method, wave_grid_min=None, wave_grid_max=24800.0,polyorder=5,
#          fit_region_min=[14000.0], fit_region_max=[16000.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)



sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut191006/Science/'
fileroots = ['J2212+2040_GNIRS','J2215+2206_GNIRS','J2224+3001_GNIRS','J2208-0744_GNIRS','P346+27_GNIRS',
             'P347+29_GNIRS','P347+27_GNIRS','J0021+0235_GNIRS','J0027+0625_GNIRS','J0144-0002_GNIRS']
#for fileroot in fileroots:
#    flux_tell(sci_path, stdfile, std_path=std_path,instrument=instrument, fileroot=fileroot, z_qso=z_qso,
#              tell_method=tell_method, wave_grid_min=None, wave_grid_max=24800.0,polyorder=5,
#              fit_region_min=[14000.0], fit_region_max=[16000.0],
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut191028/Science/'
fileroots = ['J2212+2040_GNIRS','J0035+0100_GNIRS']
for fileroot in fileroots:
    flux_tell(sci_path, stdfile, std_path=std_path,instrument=instrument, fileroot=fileroot, z_qso=z_qso,
              tell_method=tell_method, wave_grid_min=None, wave_grid_max=24800.0,polyorder=5,
              fit_region_min=[14000.0], fit_region_max=[16000.0],
              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

aaa
sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut191018/Science/'
fileroot = 'P105+29_GNIRS'
flux_tell(sci_path, stdfile, std_path=std_path,instrument=instrument, fileroot=fileroot, z_qso=z_qso,
          tell_method=tell_method, wave_grid_min=None, wave_grid_max=24800.0,polyorder=5,
          fit_region_min=[14000.0], fit_region_max=[16000.0],
          do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut191031/Science/'
fileroot = 'J0317-0611_GNIRS'
flux_tell(sci_path, stdfile, std_path=std_path,instrument=instrument, fileroot=fileroot, z_qso=z_qso,
          tell_method=tell_method, wave_grid_min=None, wave_grid_max=24800.0,polyorder=5,
          fit_region_min=[14000.0], fit_region_max=[16000.0],
          do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
