from flux_coadd_tell import flux_tell, stack_multinight



### sensfunction for GNIRS with GD71
instrument = 'GNIRS'
fileroot = 'Blue_Hawaii'
outroot = 'J1007+2115_GNIRS'
z_qso = 7.5

std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/SENSFUNC'

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
          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)

aaaa


sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/BlueHawaii/Stack'
stdfiles = ['spec1d_cN20161014S0481-GD71_GNIRS_2016Oct14T152107.457.fits']
star_ra='05:52:27.61'
star_dec='+15:53:13.8'

outroot = 'J1007+2115_GNIRS'
tell_method = 'qso'
fileroots = ['Blue_Hawaii']
for ii in range(len(fileroots)):
    fileroot = fileroots[ii]
    stdfile = stdfiles[ii]
    flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
              star_ra=star_ra, star_dec=star_dec,
              do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)


### sensfunction for NIRES
instrument = 'NIRES'

sci_path = '/Users/feige/Dropbox/OBS_DATA/NIRES/ut190519/Science'
stdfiles = ['spec1d_s190519_0059-GD153_NIRES_2019May19T083811.995.fits']
star_ra='12:57:02.34'
star_dec='+22:01:52.7'

qsoname = 'J1007'
z_qso = 7.5
tell_method = 'qso'
fileroots = ['J1007+2115_NIRES']
for ii in range(len(fileroots)):
    fileroot = fileroots[ii]
    stdfile = stdfiles[ii]
    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
              star_ra=star_ra, star_dec=star_dec,
              do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)



### Stack spectra obtained from all three nights !!!
# I used median scale since the poly scale will generate a weird dip in H-band. I think that might caused by the very
# different seeing between the three exposures. Median will basically taking the shape of data in Oct 1st which has the
# best seeing!
#outroot = qsoname+'_'+instrument
#sci_path = '/Users/feige/Dropbox/OBS_DATA/NIRES/FSpec/J0252m0503'
#stack_multinight(sci_path, 'J0252', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 scale_method='median', sn_smooth_npix=None, debug=True, show=True)