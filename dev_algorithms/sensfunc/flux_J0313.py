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
#stack_multinight(sci_path, outroot=outroot, spec1dfiles=spec1dfiles, objids=None, wave_method='log10', dv=100.0,
#                 ex_value='OPT', scale_method='poly', ivar_weights=False, sn_smooth_npix=None, debug=True, show=True)

## J0313-1806 FLAMINGOS data
### sensfunction for MOSFIRE
instrument = 'FLAMINGOS2'
std_path = os.path.join(basedir,'Dropbox/OBS_DATA/FLAMINGOS/SENSFUNC')
stdfile = 'spec1d_S20191118S0196-HD27476_FLAMINGOS_2019Nov18T044652.500.fits'
sci_path = os.path.join(basedir,'Dropbox/OBS_DATA/FLAMINGOS/J0313-1806')

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
               'spec1d_S20191121S0227-J0313-1806_FLAMINGOS_2019Nov21T071307.500.fits',
               'spec1d_S20191211S0278-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0279-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0282-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0283-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0286-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0287-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0290-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0291-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0294-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0295-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0298-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0299-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0302-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0303-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0306-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0307-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0310-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits',
               'spec1d_S20191211S0311-J0313-1806_FLAMINGOS_2019Dec11T044652.500.fits']
objids = ['SPAT0978-SLIT0000-DET01','SPAT1089-SLIT0000-DET01','SPAT0978-SLIT0000-DET01','SPAT1089-SLIT0000-DET01',
          'SPAT0978-SLIT0000-DET01','SPAT1089-SLIT0000-DET01','SPAT0978-SLIT0000-DET01','SPAT1088-SLIT0000-DET01',
          'SPAT1088-SLIT0000-DET01','SPAT0978-SLIT0000-DET01','SPAT0977-SLIT0000-DET01', 'SPAT1088-SLIT0000-DET01',
          'SPAT0978-SLIT0000-DET01','SPAT1088-SLIT0000-DET01','SPAT0977-SLIT0000-DET01', 'SPAT1088-SLIT0000-DET01',
          'SPAT0978-SLIT0000-DET01','SPAT1088-SLIT0000-DET01','SPAT0977-SLIT0000-DET01', 'SPAT1088-SLIT0000-DET01',
          'SPAT0978-SLIT0000-DET01','SPAT1088-SLIT0000-DET01','SPAT0977-SLIT0000-DET01', 'SPAT1088-SLIT0000-DET01',
          'SPAT0977-SLIT0000-DET01','SPAT1088-SLIT0000-DET01','SPAT0977-SLIT0000-DET01', 'SPAT1087-SLIT0000-DET01']
flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, spec1dfiles=spec1dfiles, objids=objids,
          outroot=outroot, z_qso=z_qso, tell_method=tell_method, star_type='A0V', star_mag=8.73,sens_polyorder=8,
          wave_grid_min=13640., wave_grid_max=25200.,
          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)
