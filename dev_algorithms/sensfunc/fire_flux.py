import os
from flux_coadd_tell import flux_tell, stack_multinight

### sensfunction for FIRE
instrument = 'FIRE'


#basedir = '/d2/Feige/'
basedir = os.getenv('HOME')

std_path = os.path.join(basedir,'Dropbox/OBS_DATA/FIRE/Echelle/SENSFUNC')
stdfile = 'spec1d_fire_0162-GD71_FIRE_8590Nov02T204709.000.fits'

tell_method = 'qso'

## J0313-1806
sci_path = os.path.join(basedir,'Dropbox/OBS_DATA/FIRE/Echelle/J0313m1806')
z_qso = 7.65
fileroot = 'J0313-1806_FIRE'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso,
#          tell_method=tell_method,
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)

## J1007+2115
sci_path = os.path.join(basedir,'Dropbox/OBS_DATA/FIRE/Echelle/J1007p2125')
z_qso = 7.51
fileroot = 'J1007+2115_FIRE'
flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso,
          tell_method=tell_method,
          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)

## J0038-0653
sci_path = os.path.join(basedir,'Dropbox/OBS_DATA/FIRE/Echelle/J0038m0653')
z_qso = 7.1
tell_method = 'qso'
fileroot = 'J0038-0653_FIRE'
flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso,
          tell_method=tell_method,
          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)


### OLD
aaaa
## J0100+2802
qsoname = 'J0100+2802'
sci_path = '/Users/feige/Desktop/FIRE_J0100/Science'
# Note this is a A5 star, I just using it as an example.
# Do NOT use for your science!!!!
stdfile = 'spec1d_fire_0036-HIP116886_FIRE_8585Sep28T182734.000.fits'
z_qso = 6.30
tell_method = 'qso'
fileroot = 'J0100_hz6_FIRE'
#flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#          star_type='A0', star_mag=9.92,
#          do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)



### Longslit
## J0313-1806
qsoname = 'J0313-1806'
sci_path = '/Users/feige/Desktop/FIRE1911/Longslit/ut191112/Science'
stdfile = 'spec1d_fire_0249-HD25266_FIRE_8590Nov03T174926.000.fits'
z_qso = 7.65
tell_method = 'qso'
outroot = 'J0313-1806_FIRE_Long'
spec1dfiles = ['spec1d_fire_0243-J0313_FIRE_8590Nov03T164525.000.fits',
               'spec1d_fire_0245-J0313_FIRE_8590Nov03T171339.000.fits',
               'spec1d_fire_0244-J0313_FIRE_8590Nov03T170110.000.fits',
               'spec1d_fire_0246-J0313_FIRE_8590Nov03T172750.000.fits',
               'spec1d_fire_0066-J0313-1806_FIRE_8590Oct27T194521.000.fits']
objids = ['SPAT0155-SLIT0000-DET01','SPAT0215-SLIT0000-DET01','SPAT0215-SLIT0000-DET01','SPAT0155-SLIT0000-DET01',
          'SPAT0186-SLIT0000-DET01']
###  In telluric Line 1042       mask_tot = mask & qsomask & (wave<15000.0)
#flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, outroot=outroot, z_qso=z_qso, tell_method=tell_method,
#          spec1dfiles=spec1dfiles, objids=objids, star_type='A0V', star_mag=9.88,sens_polyorder=5,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)

