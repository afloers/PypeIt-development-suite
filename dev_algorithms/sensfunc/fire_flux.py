from flux_coadd_tell import flux_tell, stack_multinight

### sensfunction for FIRE
instrument = 'FIRE'

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

## J0313-1806
qsoname = 'J0313-1806'
sci_path = '/Users/feige/Desktop/FIRE1911/Echelle/Science'
stdfile = 'spec1d_fire_0059-HD2641_FIRE_8590Oct27T171921.000.fits'
z_qso = 7.65
tell_method = 'qso'
fileroot = 'J0313-1806_FIRE'
flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
          star_type='A0', star_mag=9.48,
          do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## J0038-0653
qsoname = 'J0038-0653'
z_qso = 7.1
tell_method = 'qso'
fileroot = 'J0038-0653_FIRE'
flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
          star_type='A0', star_mag=9.48,
          do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

