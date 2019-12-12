import os
from flux_coadd_tell import flux_tell, stack_multinight


#basedir = '/d2/Feige/'
basedir = os.getenv('HOME')


tell_method = 'qso'
z_qso = 7.62

### J0313-1806 NIRES data
instrument = 'NIRES'
std_path = os.path.join(basedir,'Dropbox/OBS_DATA/NIRES/SENSFUNC')
stdfile = 'spec1d_s190519_0059-GD153_NIRES_2019May19T083811.995.fits'
sci_path = os.path.join(basedir,'Dropbox/OBS_DATA/NIRES/ut191111/Science')
fileroot = 'J0313-1806_NIRES'
outroot = 'J0313-1806_NIRES'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso,
#          tell_method=tell_method, outroot=outroot,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)


outroot = 'J0313-1806_NIRES_dv50kms'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso,
#          tell_method=tell_method, outroot=outroot, dv=50.,
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)

## J0313-1806 FIRE data
instrument = 'FIRE'
std_path = os.path.join(basedir, 'Dropbox/OBS_DATA/FIRE/Echelle/SENSFUNC')
stdfile = 'spec1d_fire_0162-GD71_FIRE_8590Nov02T204709.000.fits'
sci_path = os.path.join(basedir,'Dropbox/OBS_DATA/FIRE/Echelle/J0313m1806')
fileroot = 'J0313-1806_FIRE'
outroot = 'J0313-1806_FIRE'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso,
#          tell_method=tell_method, outroot=outroot,
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)

outroot = 'J0313-1806_FIRE_dv50kms'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso,
#          tell_method=tell_method, outroot=outroot, dv=50.,
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)

### Stack spectra obtained from FIRE and NIRES
outroot = 'J0313-1806_FIRE_NIRES'
sci_path = os.path.join(basedir,'Dropbox/OBS_DATA/J0313/FIRE_NIRES')
spec1dfiles = ['J0313-1806_FIRE_dv50kms_tellcorr.fits','J0313-1806_NIRES_dv50kms_tellcorr.fits']
stack_multinight(sci_path, outroot=outroot, spec1dfiles=spec1dfiles, objids=None, wave_method='log10', dv=100.0,
                 ex_value='OPT', scale_method='poly', ivar_weights=False, sn_smooth_npix=None, debug=True, show=True)
