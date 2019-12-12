from flux_coadd_tell import flux_tell, stack_multinight, merge_vis_nir

### sensfunction for NIR arm
instrument = 'XSHOOTER_NIR'

## J0020-3653
qsoname = 'J0020-3653'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
stdfiles = ['spec1d_XSHOO.2017-10-25T23:32:05.543-LTT7987_XShooter_NIR_2017Oct25T233205.543.fits']
z_qso = 6.85
tell_method = 'qso'
fileroots = ['J0020-3653_XShooter_NIR_2017']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=True, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

qsoname = 'J0100+2802'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J0100', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 wave_grid_max=20500., sn_smooth_npix=None, debug=False, show=True)

## merge VIS and NIR
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/FSpec'
spec1dvis = 'J0100+2802_XSHOOTER_VIS.fits'
spec1dnir = 'J0100+2802_XSHOOTER_NIR.fits'
outfile = qsoname+'_XShooter.fits'
stack_region = [10100.0,10280.0]
merge_vis_nir(outfile, spec1dvis, spec1dnir, sci_path=sci_path, stack_region=stack_region,
              scale_method='median')

# J0224-4711
qsoname = 'J0224-4711'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
stdfiles = ['spec1d_XSHOO.2017-11-23T08:25:54.754-LTT3218_XShooter_NIR_2017Nov23T082554.754.fits',
            'spec1d_XSHOO.2017-11-23T08:25:54.754-LTT3218_XShooter_NIR_2017Nov23T082554.754.fits']
#BAD STD            'spec1d_XSHOO.2018-01-20T02:01:09.720-GD71_XShooter_NIR_2018Jan20T020109.720.fits']
z_qso = 6.51
tell_method = 'qso'
fileroots = ['J0224-4711_XShooter_NIR_2017Nov','J0224-4711_XShooter_NIR_2018Jan']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)
### Decide to combine first!!!
stdfile = 'spec1d_XSHOO.2017-11-23T08:25:54.754-LTT3218_XShooter_NIR_2017Nov23T082554.754.fits'
fileroot = 'J0224-4711_XShooter_NIR'
#flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)


# J0226+0302
qsoname = 'J0226+0302'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
stdfiles = ['spec1d_XSHOO.2017-12-17T08:16:53.582-LTT3218_XShooter_NIR_2017Dec17T081653.582.fits',
            'spec1d_XSHOO.2017-12-17T08:16:53.582-LTT3218_XShooter_NIR_2017Dec17T081653.582.fits']
#BAD STD            'spec1d_XSHOO.2018-01-14T00:55:22.889-GD71_XShooter_NIR_2018Jan14T005522.889.fits']
z_qso = 6.54
tell_method = 'qso'
fileroots = ['J0226+0302_XShooter_NIR_2017Dec','J0226+0302_XShooter_NIR_2018Jan']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)
stdfile = 'spec1d_XSHOO.2017-12-17T08:16:53.582-LTT3218_XShooter_NIR_2017Dec17T081653.582.fits'
fileroot = 'J0226+0302_XShooter_NIR'
#flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)


## J0252-0503
qsoname = 'J0252-0503'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
stdfiles = ['spec1d_XSHOO.2019-08-04T23:19:17.990-EG274_XShooter_NIR_2019Aug04T231917.990.fits']
z_qso = 7.0
tell_method = 'qso'
fileroots = ['J0252-0503_XShooter_NIR_2019Aug']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

qsoname = 'J0439+1634'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J0439', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)
## merge VIS and NIR
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/FSpec'
spec1dvis = 'J0439+1634_XSHOOTER_VIS.fits'
spec1dnir = 'J0439+1634_XSHOOTER_NIR.fits'
qsoname = 'J0439+1634'
outfile = qsoname+'_XShooter.fits'
stack_region = [10100.0,10280.0]
#merge_vis_nir(outfile, spec1dvis, spec1dnir, sci_path=sci_path, stack_region=stack_region,
#              scale_method='median')


## J1110-1329
qsoname = 'J1110-1329'
std_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/J1629+2407/NIR/Science/'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
stdfile = 'spec1d_XSHOO.2017-06-19T10:03:36.553-Feige110_XShooter_NIR_2017Jun19T100336.553.fits'
z_qso = 6.51
tell_method = 'qso'
fileroot = 'J167m13_XShooter_NIR'
outroot = 'J1110-1329_XShooter_NIR'
#flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#          std_path=std_path, outroot=outroot,
#          do_sens=True, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

# J1212+0505
qsoname = 'J1212+0505'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
#BAD STD 'spec1d_XSHOO.2018-02-23T23:54:47.816-GD71_XShooter_NIR_2018Feb23T235447.816.fits',
stdfiles = ['spec1d_XSHOO.2018-03-16T09:17:50.437-EG274_XShooter_NIR_2018Mar16T091750.437.fits',
            'spec1d_XSHOO.2018-03-16T09:17:50.437-EG274_XShooter_NIR_2018Mar16T091750.437.fits']
z_qso = 6.43
tell_method = 'qso'
fileroots = ['PSOJ183p05_XShooter_NIR_2018Feb','PSOJ183p05_XShooter_NIR_2018Mar']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)
stdfile = 'spec1d_XSHOO.2018-03-16T09:17:50.437-EG274_XShooter_NIR_2018Mar16T091750.437.fits'
fileroot = 'PSOJ183p05_XShooter_NIR'
outroot = 'J1212+0505_XShooter_NIR'
#flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, outroot=outroot, z_qso=z_qso, tell_method=tell_method,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)


# J1526-2049
qsoname = 'J1526-2049'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
z_qso = 6.43
tell_method = 'qso'
stdfile = 'spec1d_XSHOO.2018-03-16T09:17:50.437-EG274_XShooter_NIR_2018Mar16T091750.437.fits'
fileroot = 'PSOJ183p05_XShooter_NIR'
outroot = 'J1212+0505_XShooter_NIR'
#flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, outroot=outroot, z_qso=z_qso, tell_method=tell_method,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)


## J1629+2407
qsoname = 'J1629+2407'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
stdfiles = ['spec1d_XSHOO.2017-03-25T23:21:47.701-LTT3218_XShooter_NIR_2017Mar25T232147.701.fits',
            'spec1d_XSHOO.2017-04-07T09:14:42.232-LTT7987_XShooter_NIR_2017Apr07T091442.232.fits',
            'spec1d_XSHOO.2017-06-19T01:21:19.630-EG274_XShooter_NIR_2017Jun19T012119.630.fits']
z_qso = 6.47
tell_method = 'qso'
fileroots = ['PSOJ247p24_XShooter_NIR_2017Mar','PSOJ247p24_XShooter_NIR_2017Apr','PSOJ247p24_XShooter_NIR_2017Jun']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=True, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
stdfile = stdfiles[0]
fileroot = 'PSOJ247p24_XShooter_NIR'
outroot = 'J1629+2407_XShooter_NIR'
#flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#          outroot=outroot,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)
outroot = 'J1629+2407_XShooter_NIR_ALL'
## ToDo: Need to debug stack_multinight
#stack_multinight(sci_path, 'PSOJ247p24_XShooter_NIR', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=True, show=True)


## J2211-3206
qsoname = 'J2211-3206'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
stdfiles = ['spec1d_XSHOO.2015-10-24T23:39:57.538-LTT7987_XShooter_NIR_2015Oct24T233957.538.fits']
z_qso = 6.33
tell_method = 'qso'
fileroots = ['J2211m3206_XShooter_NIR']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=False)

## J2211-6320
qsoname = 'J2211-6320'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
stdfiles = ['spec1d_XSHOO.2019-06-08T23:19:30.578-LTT3218_XShooter_NIR_2019Jun08T231930.578.fits',
            'spec1d_XSHOO.2019-08-22T06:02:23.831-Feige110_XShooter_NIR_2019Aug22T060223.831.fits']
z_qso = 6.86
tell_method = 'qso'
fileroots = ['J2211-6320_XShooter_NIR_2019Jun','J2211-6320_XShooter_NIR_2019Aug']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## J2348-3054
qsoname = 'J2348-3054'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/{:}/NIR/Science'.format(qsoname,qsoname)
stdfiles = ['spec1d_XSHOO.2011-08-20T23:33:01.643-LTT7987_XShooter_NIR_2011Aug20T233301.643.fits']
z_qso = 6.90
tell_method = 'qso'
fileroots = ['J2348-3054_XShooter_NIR_2011']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=True, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)


