from flux_coadd_tell import flux_tell, stack_multinight

### sensfunction for GNIRS with GD71
instrument = 'GNIRS'
fileroot = 'Blue_Hawaii'
outroot = 'J1007+2115_GNIRS_NewGrid'
z_qso = 7.5

std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/SENSFUNC'

stdfile = 'spec1d_cN20161014S0481-GD71_GNIRS_2016Oct14T152107.457.fits'
star_ra='05:52:27.61'
star_dec='+15:53:13.8'

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/BlueHawaii/Stack_GD71_NewGrid'
tell_method = 'qso'
fileroot = 'Blue_Hawaii_GNIRS'
outroot = 'J1007+2115_GNIRS_GD71_NewGrid_Final'
flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
          outroot=outroot, star_ra=star_ra, star_dec=star_dec, sens_polyorder=8,
          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=False)
aaaa

### Stack spectra obtained from GNIRS and NIRES
outroot = 'J1007+2115_NIRES_GNIRS'
#fileroot = 'NewGrid_tellcorr'
sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/BlueHawaii/NIRES_GNIRS'
spec1dfiles = ['J1007+2115_GNIRS_GD71_NewGrid_tellcorr.fits','J1007+2115_NIRES_NewGrid_tellcorr.fits']
stack_multinight(sci_path, outroot=outroot, spec1dfiles=spec1dfiles, objids=None, wave_method='log10', dv=100.0,
                 ex_value='OPT', scale_method='poly', sn_smooth_npix=None, debug=True, show=True)

aaa

### sensfunction for NIRES
instrument = 'NIRES'

sci_path = '/Users/feige/Dropbox/OBS_DATA/NIRES/ut190519/Science'
stdfile = 'spec1d_s190519_0059-GD153_NIRES_2019May19T083811.995.fits'
star_ra='12:57:02.34'
star_dec='+22:01:52.7'

qsoname = 'J1007'
z_qso = 7.5
tell_method = 'qso'
fileroot = 'J1007+2115_NIRES'
outroot = 'J1007+2115_NIRES_NewGrid'
flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, outroot=outroot, z_qso=z_qso,
          tell_method=tell_method, star_ra=star_ra, star_dec=star_dec,
          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)

aaaa




sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190531/Science/'
##stdfile = 'spec1d_N20190531S0007-HIP50459_GNIRS_2019May31T043733.507.fits'
##flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=6.523,
##          fileroot = fileroot, outroot = outroot,
##          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)
stdfile = 'spec1d_N20190531S0067-HIP56736_GNIRS_2019May31T073323.707.fits'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          fileroot=fileroot, outroot=outroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190601/Science/'
stdfile = 'spec1d_N20190601S0171-HIP56736_GNIRS_2019Jun01T074502.552.fits'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          fileroot=fileroot, outroot=outroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190602/Science/'
stdfile = 'spec1d_N20190602S0113-HIP56736_GNIRS_2019Jun02T074159.955.fits'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          fileroot=fileroot, outroot=outroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190611/Science/'
stdfile = 'spec1d_N20190611S0066-HIP56736_GNIRS_2019Jun11T040455.775.fits'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          fileroot=fileroot, outroot=outroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190612/Science/'
stdfile = 'spec1d_N20190612S0042-HIP56736_GNIRS_2019Jun12T030250.192.fits'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          fileroot=fileroot, outroot=outroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190613/Science/'
stdfile = 'spec1d_N20190613S0087-HIP56736_GNIRS_2019Jun13T021538.575.fits'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          fileroot=fileroot, outroot=outroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)


sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/BlueHawaii/Stack_A0'
flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
          fileroot=fileroot, outroot=outroot,z_qso=z_qso,
          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)

aaaa






