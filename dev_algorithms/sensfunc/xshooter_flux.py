from dev_flux_tell import flux_tell, stack_multinight, merge_vis_nir

### sensfunction for VIS arm
instrument = 'XSHOOTER_VIS'

## J0020-3653
qsoname = 'J0020-3653'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2017-10-25T23:32:02.407-LTT7987_XShooter_VIS_2017Oct25T233202.407.fits',
            'spec1d_XSHOO.2017-10-25T23:32:02.407-LTT7987_XShooter_VIS_2017Oct25T233202.407.fits']
            #'spec1d_XSHOO.2017-10-25T23:37:51.508-LTT7987_XShooter_VIS_2017Oct25T233751.509.fits']
z_qso = 6.85
tell_method = 'qso'
fileroots = ['J0020-3653_XShooter_VIS_2017Oct26','J0020-3653_XShooter_VIS_2017Dec17']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=True, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, qsoname, outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                     sn_smooth_npix=None, debug=False, show=True)
### combine first and then telluric
### ToDo seems combine first and then telluric is better due to it has better rejections.
stdfiles = ['spec1d_XSHOO.2017-10-25T23:32:02.407-LTT7987_XShooter_VIS_2017Oct25T233202.407.fits']
fileroots = ['J0020-3653_XShooter_VIS_2017']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

# merge VIS and NIR
spec1dvis = 'J0020-3653_XShooter_VIS_2017_tellcorr_scale.fits'
spec1dnir = 'J0020-3653_XShooter_NIR_2017_tellcorr_scale.fits'
qsoname = 'J0020-3653'
outfile = qsoname+'_XShooter.fits'
sci_path = '/Users/feige/Dropbox/QSO_DATA/DP_Spec/J0020-3653'
stack_region = [10150.0,10200.0]
#merge_vis_nir(outfile, spec1dvis, spec1dnir, sci_path=sci_path, stack_region=stack_region)

## J0109-3047
qsoname = 'J0109-3047'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2011-08-20T09:53:04.321-Feige110_XShooter_VIS_2011Aug20T095304.321.fits',
            'spec1d_XSHOO.2011-08-20T09:53:04.321-Feige110_XShooter_VIS_2011Aug20T095304.321.fits',
            'spec1d_XSHOO.2011-12-22T00:21:30.342-Feige110_XShooter_VIS_2011Dec22T002130.341.fits']
z_qso = 6.75
tell_method = 'qso'
fileroots = ['J0109-3047_XShooter_VIS_2011Aug20','J0109-3047_XShooter_VIS_2011Aug22',
             'J0109-3047_XShooter_VIS_2011Nov25']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, qsoname, outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                     sn_smooth_npix=None, debug=False, show=True)

## J0100+2802
qsoname = 'J0100+2802'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J0100', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)


## J0142-3327
qsoname = 'J0142-3327'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2015-10-21T08:57:55.950-LTT3218_XShooter_VIS_2015Oct21T085755.950.fits',
            'spec1d_XSHOO.2015-11-19T23:46:57.778-Feige110_XShooter_VIS_2015Nov19T234657.777.fits']
z_qso = 6.32
tell_method = 'qso'
fileroots = ['J25.6821-33.4627_XShooter_VIS_2015Oct21','J25.6821-33.4627_XShooter_VIS_2015Nov20']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J25.6821-33.4627', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=True, show=True)
## combine first and then telluric
### ToDo seems combine first and then telluric is better due to it has better rejections.
stdfiles = ['spec1d_XSHOO.2015-10-21T08:57:55.950-LTT3218_XShooter_VIS_2015Oct21T085755.950.fits']
fileroots = ['J25.6821-33.4627_XShooter_VIS']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=True, debug=False)

## J0224-4711
qsoname = 'J0224-4711'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2017-11-23T08:25:51.567-LTT3218_XShooter_VIS_2017Nov23T082551.567.fits',
            'spec1d_XSHOO.2018-01-18T08:43:18.841-LTT3218_XShooter_VIS_2018Jan18T084318.841.fits']
z_qso = 6.51
tell_method = 'qso'
fileroots = ['J0224-4711_XShooter_VIS_2017Nov23','J0224-4711_XShooter_VIS_2018Jan19']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, qsoname, outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)

## J0226+0302
qsoname = 'J0226+0302'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2017-12-17T08:16:50.483-LTT3218_XShooter_VIS_2017Dec17T081650.483.fits',
            'spec1d_XSHOO.2018-01-14T00:42:27.513-GD71_XShooter_VIS_2018Jan14T004227.513.fits']
z_qso = 6.54
tell_method = 'qso'
fileroots = ['J0226+0302_XShooter_VIS_2017Dec17','J0226+0302_XShooter_VIS_2018Jan14']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=True, debug=False)
#outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, qsoname, outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)

## J0252-0503
qsoname = 'J0252-0503'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2019-08-04T23:19:14.937-EG274_XShooter_VIS_2019Aug04T231914.937.fits',
            'spec1d_XSHOO.2019-08-04T23:19:14.937-EG274_XShooter_VIS_2019Aug04T231914.937.fits']
z_qso = 7.0
tell_method = 'qso'
fileroots = ['J0252-0503_XShooter_VIS_2019Aug06','J0252-0503_XShooter_VIS_2019Aug11']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=True, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, qsoname, outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)
### combine first and then telluric
### ToDo seems combine first and then telluric is better due to it has better rejections.
stdfiles = ['spec1d_XSHOO.2019-08-04T23:19:14.937-EG274_XShooter_VIS_2019Aug04T231914.937.fits']
fileroots = ['J0252-0503_XShooter_VIS_2019Aug']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)

## J0305-3150
qsoname = 'J0305-3150'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2016-10-21T08:43:57.556-LTT3218_XShooter_VIS_2016Oct21T084357.556.fits',
            'spec1d_XSHOO.2016-11-01T23:41:14.083-LTT7987_XShooter_VIS_2016Nov01T234114.083.fits',
            'spec1d_XSHOO.2016-11-03T23:41:52.773-LTT7987_XShooter_VIS_2016Nov03T234152.772.fits',
            'spec1d_XSHOO.2016-11-05T23:41:10.105-Feige110_XShooter_VIS_2016Nov05T234110.105.fits',
            'spec1d_XSHOO.2016-11-20T06:35:21.428-GD71_XShooter_VIS_2016Nov20T063521.428.fits',
            'spec1d_XSHOO.2016-11-28T00:03:09.905-Feige110_XShooter_VIS_2016Nov28T000309.905.fits']
z_qso = 6.61
tell_method = 'qso'
fileroots = ['J0305m3150_XShooter_VIS_2016Oct21','J0305m3150_XShooter_VIS_2016Nov02',
             'J0305m3150_XShooter_VIS_2016Nov04','J0305m3150_XShooter_VIS_2016Nov06',
             'J0305m3150_XShooter_VIS_2016Nov20','J0305m3150_XShooter_VIS_2016Nov28']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=True, debug=False)
#outroot = qsoname+'_'+instrument+'_ALL'
#stack_multinight(sci_path, 'J0305m3150', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)
spec1dfiles = ['J0305m3150_XShooter_VIS_2016Nov02_tellcorr.fits',
               'J0305m3150_XShooter_VIS_2016Nov06_tellcorr.fits',
               'J0305m3150_XShooter_VIS_2016Nov20_tellcorr.fits',
               'J0305m3150_XShooter_VIS_2016Nov28_tellcorr.fits',
               'J0305m3150_XShooter_VIS_2016Oct21_tellcorr.fits']
#outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J0305m3150', outroot=outroot, spec1dfiles=spec1dfiles, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)

## J0439+1634
qsoname = 'J0439+1634'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/reduced/VIS/Science'.format(qsoname)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J0439', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)

## J1030+0524
qsoname = 'J1030+0524'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_SHOOT.2009-12-23T09:12:19.248-GD153_XShooter_VIS_2009Dec23T091219.248.fits',
            'spec1d_XSHOO.2011-02-24T00:01:08.393-LTT3218_XShooter_VIS_2011Feb24T000108.393.fits',
            'spec1d_XSHOO.2011-02-24T00:01:08.393-LTT3218_XShooter_VIS_2011Feb24T000108.393.fits',
            'spec1d_XSHOO.2011-05-31T22:45:22.894-LTT3218_XShooter_VIS_2011May31T224522.894.fits',
            'spec1d_XSHOO.2011-06-01T22:33:28.831-LTT3218_XShooter_VIS_2011Jun01T223328.831.fits']
z_qso = 6.30
tell_method = 'qso'
fileroots = ['J103027.10+052455.1_XShooter_VIS_2009Dec23','J1030+0524_XShooter_VIS_2011Feb08',
             'J103027+052455_XShooter_VIS_2011Mar03','J1030+0524_XShooter_VIS_2011May31',
             'J1030+0524_XShooter_VIS_2011Jun01']
objids = {'0':['OBJ0001','OBJ0001','OBJ0001','OBJ0001'],'1':['OBJ0001','OBJ0001','OBJ0001','OBJ0001','OBJ0001','OBJ0001','OBJ0001','OBJ0001'],
          '2':['OBJ0002','OBJ0001'],'3':['OBJ0001'],'4':['OBJ0002','OBJ0001']}
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              objids = objids[str(ii)],
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J1030', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)

## J1036-0232
qsoname = 'J1036-0232'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2017-04-03T23:17:21.979-LTT3218_XShooter_VIS_2017Apr03T231721.978.fits',
            'spec1d_XSHOO.2017-12-17T08:16:50.483-LTT3218_XShooter_VIS_2017Dec17T081650.483.fits']
z_qso = 6.38
tell_method = 'qso'
fileroots = ['J159m02_XShooter_VIS_2017Apr04','J159m02_XShooter_VIS_2017Dec17']
objids = {'0':['OBJ0001','OBJ0001'],'1':['OBJ0002','OBJ0001']}
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              objids = objids[str(ii)],
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=True, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J159m02', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=False, show=True)

## J1048-0109
qsoname = 'J1048-0109'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/J1048-0109/VIS/Science'
stdfiles = ['spec1d_XSHOO.2017-02-02T08:56:59.133-GD153_XShooter_VIS_2017Feb02T085659.133.fits']
            #'spec1d_XSHOO.2017-02-02T09:09:53.037-GD153_XShooter_VIS_2017Feb02T090953.037.fits']
z_qso = 6.66
tell_method = 'qso'
fileroots = ['J1048m0109_XShooter_VIS']
objids = {'0':['OBJ0002','OBJ0001']}
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              objids = objids[str(ii)],
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## J1110-1329
qsoname = 'J1110-1329'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2017-07-13T23:05:56.580-GD153_XShooter_VIS_2017Jul13T230556.580.fits']#,
            #'spec1d_XSHOO.2017-07-13T23:18:50.132-GD153_XShooter_VIS_2017Jul13T231850.133.fits']
z_qso = 6.51
tell_method = 'qso'
fileroots = ['J167m13_XShooter_VIS']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=True, debug=False)


## J1148+0702
qsoname = 'J1148+0702'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2017-04-05T08:20:18.681-EG274_XShooter_VIS_2017Apr05T082018.681.fits',
            'spec1d_XSHOO.2018-01-20T02:01:06.685-GD71_XShooter_VIS_2018Jan20T020106.685.fits',
            'spec1d_XSHOO.2018-02-06T09:12:46.984-EG274_XShooter_VIS_2018Feb06T091246.984.fits',
            'spec1d_XSHOO.2018-02-21T00:00:47.645-GD71_XShooter_VIS_2018Feb21T000047.645.fits']
z_qso = 6.33
tell_method = 'qso'
fileroots = ['J1148p0702_XShooter_VIS_2017Apr05','J1148p0702_XShooter_VIS_2018Jan19',
             'J1148p0702_XShooter_VIS_2018Feb06','J1148p0702_XShooter_VIS_2018Feb21']
objids = {'0':['OBJ0002','OBJ0001'],'1':['OBJ0001','OBJ0001'],
          '2':['OBJ0001','OBJ0001'],'3':['OBJ0002','OBJ0001']}
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              objids = objids[str(ii)],
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J1148', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=True, show=True)

## J1152+0055
qsoname = 'J1152+0055'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2016-06-22T22:56:12.606-GD153_XShooter_VIS_2016Jun22T225612.606.fits',
            'spec1d_XSHOO.2017-01-04T08:35:14.940-LTT3218_XShooter_VIS_2017Jan04T083514.939.fits',
            'spec1d_XSHOO.2017-02-02T08:56:59.133-GD153_XShooter_VIS_2017Feb02T085659.133.fits',
            'spec1d_XSHOO.2017-02-06T00:20:04.188-LTT3218_XShooter_VIS_2017Feb06T002004.188.fits',
            'spec1d_XSHOO.2018-03-12T09:40:33.506-EG274_XShooter_VIS_2018Mar12T094033.506.fits',
            'spec1d_XSHOO.2018-03-12T23:39:07.258-GD71_XShooter_VIS_2018Mar12T233907.258.fits',
            'spec1d_XSHOO.2018-03-14T07:31:18.811-GD153_XShooter_VIS_2018Mar14T073118.810.fits',
            'spec1d_XSHOO.2018-03-14T23:37:48.504-GD71_XShooter_VIS_2018Mar14T233748.504.fits']
z_qso = 6.36
tell_method = 'qso'
fileroots = ['J1152p0055_XShooter_VIS_2016Jun2','J1152p0055_XShooter_VIS_2017Jan04',
             'J1152p0055_XShooter_VIS_2017Feb02','J1152p0055_XShooter_VIS_2017Feb06',
             'J1152+0055_XShooter_VIS_2018Mar12','J1152+0055_XShooter_VIS_2018Mar13',
             'J1152+0055_XShooter_VIS_2018Mar14','J1152+0055_XShooter_VIS_2018Mar15']
objids = {'0':['OBJ0002','OBJ0001'],'1':['OBJ0002','OBJ0001'],
          '2':['OBJ0001','OBJ0001','OBJ0001','OBJ0001'],'3':['OBJ0001','OBJ0001'],
          '4':['OBJ0001','OBJ0001','OBJ0001','OBJ0001'],'5':['OBJ0001','OBJ0001','OBJ0001','OBJ0001','OBJ0001','OBJ0001'],
          '6':['OBJ0001','OBJ0001','OBJ0001','OBJ0001'],'7':['OBJ0001','OBJ0001']}
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              objids = objids[str(ii)],
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J1152', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=True, show=True)

## J1212+0505
qsoname = 'J1212+0505'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2018-02-23T23:54:44.833-GD71_XShooter_VIS_2018Feb23T235444.833.fits',
            'spec1d_XSHOO.2018-03-16T09:17:47.612-EG274_XShooter_VIS_2018Mar16T091747.612.fits']
z_qso = 6.43
tell_method = 'qso'
fileroots = ['J183p05_XShooter_VIS_2018Feb23','J183p05_XShooter_VIS_2018Mar16']
objids = {'0':['OBJ0002','OBJ0001'],'1':['OBJ0002','OBJ0001']}
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              objids = objids[str(ii)],
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J183', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=True, show=True)

## J1526-2049
qsoname = 'J1526-2049'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2016-07-11T23:01:09.217-GD153_XShooter_VIS_2016Jul11T230109.217.fits']#,
            #'spec1d_XSHOO.2016-07-11T23:14:01.918-GD153_XShooter_VIS_2016Jul11T231401.919.fits']
z_qso = 6.58
tell_method = 'qso'
fileroots = ['J231m20_XShooter_VIS']
objids = {'0':['OBJ0002','OBJ0001']}
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              objids = objids[str(ii)],
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## J1629+2407
qsoname = 'J1629+2407'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2017-03-25T23:21:44.486-LTT3218_XShooter_VIS_2017Mar25T232144.486.fits',
            'spec1d_XSHOO.2017-04-07T09:14:39.325-LTT7987_XShooter_VIS_2017Apr07T091439.325.fits',
            'spec1d_XSHOO.2017-06-19T01:21:16.371-EG274_XShooter_VIS_2017Jun19T012116.371.fits',
            #'spec1d_XSHOO.2017-06-19T10:03:33.284-Feige110_XShooter_VIS_2017Jun19T100333.284.fits',
            'spec1d_XSHOO.2017-07-21T09:45:58.938-Feige110_XShooter_VIS_2017Jul21T094558.938.fits',
            'spec1d_XSHOO.2017-07-23T00:37:27.772-EG274_XShooter_VIS_2017Jul23T003727.772.fits']
z_qso = 6.47
tell_method = 'qso'
fileroots = ['J247p24_XShooter_VIS_2017Mar26','J247p24_XShooter_VIS_2017Apr07',
             'J247p24_XShooter_VIS_2017Jun19','J247p24_XShooter_VIS_2017Jul22']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J247', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=True, show=True)

## J2132+1217
qsoname = 'J2132+1217'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2016-10-03T23:21:52.104-Feige110_XShooter_VIS_2016Oct03T232152.104.fits']#,
            #'spec1d_XSHOO.2016-10-04T23:20:12.386-LTT7987_XShooter_VIS_2016Oct04T232012.386.fits',
            #'spec1d_XSHOO.2016-10-08T01:46:37.154-Feige110_XShooter_VIS_2016Oct08T014637.154.fits',
            #'spec1d_XSHOO.2016-10-21T08:43:57.556-LTT3218_XShooter_VIS_2016Oct21T084357.556.fits']
z_qso = 6.58
tell_method = 'qso'
fileroots = ['J323p12_XShooter_VIS']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)


## J2211-3206
qsoname = 'J2211-3206'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2015-10-24T23:39:54.474-LTT7987_XShooter_VIS_2015Oct24T233954.473.fits',
            'spec1d_XSHOO.2016-10-04T23:20:12.386-LTT7987_XShooter_VIS_2016Oct04T232012.386.fits']
z_qso = 6.33
tell_method = 'qso'
fileroots = ['J2211m3206_XShooter_VIS_2015Oct2','J2211m3206_XShooter_VIS_2016Oct05']
objids = {'0':['OBJ0002','OBJ0001'],'1':['OBJ0003','OBJ0001']}
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              objids = objids[str(ii)],
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J2211', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=True, show=True)

## J2211-6320
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/J2211-6320/VIS/Science'
stdfiles = ['spec1d_XSHOO.2019-06-08T23:19:27.375-LTT3218_XShooter_VIS_2019Jun08T231927.375.fits',
            'spec1d_XSHOO.2019-08-22T06:07:20.738-Feige110_XShooter_VIS_2019Aug22T060720.739.fits',
            'spec1d_XSHOO.2019-08-22T06:07:20.738-Feige110_XShooter_VIS_2019Aug22T060720.739.fits']
z_qso = 6.88
tell_method = 'qso'
fileroots = ['J2211-6320_XShooter_VIS_2019Jun09', 'J2211-6320_XShooter_VIS_2019Aug25', 'J2211-6320_XShooter_VIS_2019Aug31']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)
stdfile = stdfiles[0]
spec1dfiles = ['spec1d_XSHOO.2019-06-09T09:13:48.821-J2211-6320_XShooter_VIS_2019Jun09T091348.821.fits',
               'spec1d_XSHOO.2019-06-09T09:34:55.790-J2211-6320_XShooter_VIS_2019Jun09T093455.790.fits',
               'spec1d_XSHOO.2019-08-25T02:34:51.001-J2211-6320_XShooter_VIS_2019Aug25T023451.000.fits',
               'spec1d_XSHOO.2019-08-25T02:55:59.509-J2211-6320_XShooter_VIS_2019Aug25T025559.509.fits',
               'spec1d_XSHOO.2019-08-25T03:25:08.059-J2211-6320_XShooter_VIS_2019Aug25T032508.059.fits',
               'spec1d_XSHOO.2019-08-25T03:46:15.959-J2211-6320_XShooter_VIS_2019Aug25T034615.959.fits',
               'spec1d_XSHOO.2019-08-31T03:03:38.689-J2211-6320_XShooter_VIS_2019Aug31T030338.688.fits',
               'spec1d_XSHOO.2019-08-31T03:24:47.247-J2211-6320_XShooter_VIS_2019Aug31T032447.247.fits',
               'spec1d_XSHOO.2019-08-31T03:52:15.777-J2211-6320_XShooter_VIS_2019Aug31T035215.777.fits',
               'spec1d_XSHOO.2019-08-31T04:13:21.105-J2211-6320_XShooter_VIS_2019Aug31T041321.105.fits']
fileroot = 'J2211-6320_XShooter_VIS_2019'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=False)

## J2232+2930
qsoname = 'J2232+2930'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2016-10-31T23:39:49.435-LTT7987_XShooter_VIS_2016Oct31T233949.435.fits',
            'spec1d_XSHOO.2017-06-19T01:21:16.371-EG274_XShooter_VIS_2017Jun19T012116.371.fits',
            'spec1d_XSHOO.2017-06-20T10:11:53.907-Feige110_XShooter_VIS_2017Jun20T101153.907.fits',
            'spec1d_XSHOO.2017-08-15T23:17:35.055-EG274_XShooter_VIS_2017Aug15T231735.055.fits',
            'spec1d_XSHOO.2017-09-19T09:07:23.557-GD71_XShooter_VIS_2017Sep19T090723.557.fits',
            'spec1d_XSHOO.2017-09-29T23:23:09.034-EG274_XShooter_VIS_2017Sep29T232309.033.fits']
z_qso = 6.66
tell_method = 'qso'
fileroots = ['J338p29_XShooter_VIS_2016Nov01','J338p29_XShooter_VIS_2017Jun19',
             'J338p29_XShooter_VIS_2017Jun20','J338p29_XShooter_VIS_2017Aug15',
             'J338p29_XShooter_VIS_2017Sep19','J338p29_XShooter_VIS_2017Sep29']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J338', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=True, show=True)


## J2318-3113
qsoname = 'J2318-3113'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2016-08-04T23:08:47.402-GD153_XShooter_VIS_2016Aug04T230847.401.fits',
            'spec1d_XSHOO.2016-08-25T09:46:46.023-Feige110_XShooter_VIS_2016Aug25T094646.023.fits']
z_qso = 6.43
tell_method = 'qso'
fileroots = ['J2318m3113_XShooter_VIS_2016Aug05','J2318m3113_XShooter_VIS_2016Aug25']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
outroot = qsoname+'_'+instrument
#stack_multinight(sci_path, 'J2318', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
#                 sn_smooth_npix=None, debug=True, show=True)
### ToDo seems combine first and then telluric is better due to it has better rejections.
stdfiles = ['spec1d_XSHOO.2016-08-04T23:08:47.402-GD153_XShooter_VIS_2016Aug04T230847.401.fits']
fileroots = ['J2318m3113_XShooter_VIS_2016']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## J2348-3054
qsoname = 'J2348-3054'
sci_path = '/Users/feige/Dropbox/OBS_DATA/XSHOOTER/{:}/VIS/Science'.format(qsoname)
stdfiles = ['spec1d_XSHOO.2011-08-21T10:14:39.913-Feige110_XShooter_VIS_2011Aug21T101439.913.fits',
            'spec1d_XSHOO.2011-08-22T09:57:07.714-Feige110_XShooter_VIS_2011Aug22T095707.714.fits']
z_qso = 6.90
tell_method = 'qso'
fileroots = ['J2348-3054_XShooter_VIS_2011Aug21','J2348-3054_XShooter_VIS_2011Aug22']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
##outroot = qsoname+'_'+instrument
##stack_multinight(sci_path, 'J2348', outroot=outroot, spec1dfiles=None, objids=None, wave_method='log10', ex_value='OPT',
##                 sn_smooth_npix=None, debug=True, show=True)
### combine first and then telluric
### ToDo seems combine first and then telluric is better due to it has better rejections.
stdfiles = ['spec1d_XSHOO.2011-08-21T10:14:39.913-Feige110_XShooter_VIS_2011Aug21T101439.913.fits']
fileroots = ['J2348-3054_XShooter_VIS']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
