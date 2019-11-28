from dev_flux_tell import flux_tell, stack_multinight

'''
    Note that Feige 110 seems have some problem.
    The sensfunc from GD153 and G191B2B are consistent with each other very well. Since GD153 was observed in 
    very good seeing condition, we choose GD153 as our sensfunc finally.
'''
### sensfunction for NIRES
instrument = 'NIRES'

## Night 1
sci_path = '/Users/feige/Dropbox/OBS_DATA/NIRES/ut180812/Science'
stdfiles = ['spec1d_s190519_0059-GD153_NIRES_2019May19T083811.995.fits']
star_ra='12:57:02.34'
star_dec='+22:01:52.7'
#stdfiles = ['spec1d_s190218_0030-G191B2B_NIRES_2019Feb18T050628.633.fits']
#star_ra = '05:05:30.61'
#star_dec = '+52:49:51.9'
#stdfiles = ['spec1d_s180812_0061-Feige110_NIRES_2018Aug12T095435.548.fits']
#star_ra='23:19:58.40'
#star_dec='-05:09:56.2'
qsoname = 'J0252-0503'
z_qso = 7.0
tell_method = 'qso'
fileroots = ['J0252_NIRES_2018Aug12']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              star_ra=star_ra, star_dec=star_dec,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## Night 2
sci_path = '/Users/feige/Dropbox/OBS_DATA/NIRES/ut180903/Science'
qsoname = 'J0252-0503'
z_qso = 7.0
tell_method = 'qso'
fileroots = ['J0252-0503_NIRES_2018Sep03']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              star_ra=star_ra, star_dec=star_dec,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## Night 3
sci_path = '/Users/feige/Dropbox/OBS_DATA/NIRES/ut181001/Science'
qsoname = 'J0252-0503'
z_qso = 7.0
tell_method = 'qso'
fileroots = ['J0252-0503_NIRES_2018Oct01']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              star_ra=star_ra, star_dec=star_dec,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=True, debug=False)

### Stack spectra obtained from all three nights !!!
# I used median scale since the poly scale will generate a weird dip in H-band. I think that might caused by the very
# different seeing between the three exposures. Median will basically taking the shape of data in Oct 1st which has the
# best seeing!
#outroot = qsoname+'_'+instrument
#sci_path = '/Users/feige/Dropbox/OBS_DATA/NIRES/FSpec/J0252m0503'
#stack_multinight(sci_path, 'J0252', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 scale_method='median', sn_smooth_npix=None, debug=True, show=True)