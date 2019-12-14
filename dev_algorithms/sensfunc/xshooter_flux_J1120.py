from dev_flux_tell import flux_tell

### sensfunction for VIS arm
instrument = 'XSHOOTER_VIS'


## J0100+2802
sci_path = '/d2/Feige/Dropbox/OBS_DATA/XSHOOTER/J0100+2802/VIS/Science'
stdfiles = ['spec1d_XSHOO.2015-10-22T23:44:07.671-LTT7987_XShooter_VIS_2015Oct22T234407.671.fits',
            'spec1d_XSHOO.2015-12-14T00:42:56.907-Feige110_XShooter_VIS_2015Dec14T004256.907.fits',
            'spec1d_XSHOO.2015-12-15T00:39:06.447-Feige110_XShooter_VIS_2015Dec15T003906.447.fits',
            'spec1d_XSHOO.2016-07-19T10:31:07.662-Feige110_XShooter_VIS_2016Jul19T103107.662.fits',
            'spec1d_XSHOO.2016-07-20T10:16:47.492-Feige110_XShooter_VIS_2016Jul20T101647.492.fits',
            ## BADSTD ## 'spec1d_XSHOO.2016-07-21T10:01:41.938-Feige110_XShooter_VIS_2016Jul21T100141.938.fits',
            'spec1d_XSHOO.2016-07-21T10:06:42.092-Feige110_XShooter_VIS_2016Jul21T100642.092.fits',
            'spec1d_XSHOO.2016-07-28T01:37:09.128-LTT7987_XShooter_VIS_2016Jul28T013709.128.fits',
            'spec1d_XSHOO.2016-07-28T10:04:04.358-Feige110_XShooter_VIS_2016Jul28T100404.359.fits',
            'spec1d_XSHOO.2016-07-30T08:35:40.034-Feige110_XShooter_VIS_2016Jul30T083540.034.fits',
            'spec1d_XSHOO.2016-07-31T05:32:58.055-Feige110_XShooter_VIS_2016Jul31T053258.055.fits',
            'spec1d_XSHOO.2016-08-01T04:10:57.738-LTT7987_XShooter_VIS_2016Aug01T041057.739.fits',
            'spec1d_XSHOO.2016-08-01T23:12:40.572-EG274_XShooter_VIS_2016Aug01T231240.572.fits']
#for ii in range(len(stdfiles)):
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, do_sens=True, do_flux=False, do_stack=False, do_tell=False,
#              disp=False, debug=False)
z_qso = 6.30
tell_method = 'qso'
stdfiles = ['spec1d_XSHOO.2015-10-22T23:44:07.671-LTT7987_XShooter_VIS_2015Oct22T234407.671.fits',
            'spec1d_XSHOO.2015-12-14T00:42:56.907-Feige110_XShooter_VIS_2015Dec14T004256.907.fits',
            'spec1d_XSHOO.2015-12-15T00:39:06.447-Feige110_XShooter_VIS_2015Dec15T003906.447.fits',
            'spec1d_XSHOO.2016-07-19T10:31:07.662-Feige110_XShooter_VIS_2016Jul19T103107.662.fits',
            'spec1d_XSHOO.2016-07-20T10:16:47.492-Feige110_XShooter_VIS_2016Jul20T101647.492.fits',
            'spec1d_XSHOO.2016-07-21T10:06:42.092-Feige110_XShooter_VIS_2016Jul21T100642.092.fits',
            'spec1d_XSHOO.2016-07-28T10:04:04.358-Feige110_XShooter_VIS_2016Jul28T100404.359.fits',
            'spec1d_XSHOO.2016-07-30T08:35:40.034-Feige110_XShooter_VIS_2016Jul30T083540.034.fits',
            'spec1d_XSHOO.2016-07-31T05:32:58.055-Feige110_XShooter_VIS_2016Jul31T053258.055.fits',
            'spec1d_XSHOO.2016-08-01T04:10:57.738-LTT7987_XShooter_VIS_2016Aug01T041057.739.fits',
            'spec1d_XSHOO.2016-08-01T23:12:40.572-EG274_XShooter_VIS_2016Aug01T231240.572.fits']
fileroots = ['J0100p2802_XShooter_VIS_2015Oct23','J0100p2802_XShooter_VIS_2015Dec14','J0100p2802_XShooter_VIS_2015Dec15',
             'J0100p2802_XShooter_VIS_2016Jul19','J0100p2802_XShooter_VIS_2016Jul20','J0100p2802_XShooter_VIS_2016Jul21',
             'J0100p2802_XShooter_VIS_2016Jul28','J0100p2802_XShooter_VIS_2016Jul30','J0100p2802_XShooter_VIS_2016Jul31',
             'J0100p2802_XShooter_VIS_2016Aug01','J0100p2802_XShooter_VIS_2016Aug02']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## J0439+1634
sci_path = '/d2/Feige/Dropbox/OBS_DATA/XSHOOTER/J0439+1634/reduced/VIS/Science'
stdfiles = ['spec1d_XSHOO.2018-10-08T23:48:23.738-LTT7987_XShooter_VIS_2018Oct08T234823.738.fits',
            'spec1d_XSHOO.2018-10-13T23:56:00.636-LTT7987_XShooter_VIS_2018Oct13T235600.636.fits',
            'spec1d_XSHOO.2018-10-14T23:26:20.224-LTT7987_XShooter_VIS_2018Oct14T232620.224.fits',
            'spec1d_XSHOO.2018-10-16T08:34:02.733-LTT7987_XShooter_VIS_2018Oct16T083402.733.fits',
            'spec1d_XSHOO.2018-10-28T23:47:27.542-LTT7987_XShooter_VIS_2018Oct28T234727.543.fits',
            'spec1d_XSHOO.2018-11-08T00:11:54.072-Feige110_XShooter_VIS_2018Nov08T001154.072.fits',
            'spec1d_XSHOO.2018-11-12T00:04:37.190-LTT7987_XShooter_VIS_2018Nov12T000437.190.fits']
#for ii in range(len(stdfiles)):
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, do_sens=True, do_flux=False, do_stack=False, do_tell=False,
#              disp=False, debug=False)
stdfiles = ['spec1d_XSHOO.2018-10-08T23:48:23.738-LTT7987_XShooter_VIS_2018Oct08T234823.738.fits',
            'spec1d_XSHOO.2018-10-13T23:56:00.636-LTT7987_XShooter_VIS_2018Oct13T235600.636.fits',
            'spec1d_XSHOO.2018-10-14T23:26:20.224-LTT7987_XShooter_VIS_2018Oct14T232620.224.fits',
            'spec1d_XSHOO.2018-10-16T08:34:02.733-LTT7987_XShooter_VIS_2018Oct16T083402.733.fits',
            'spec1d_XSHOO.2018-10-28T23:47:27.542-LTT7987_XShooter_VIS_2018Oct28T234727.543.fits',
            'spec1d_XSHOO.2018-11-08T00:11:54.072-Feige110_XShooter_VIS_2018Nov08T001154.072.fits',
            'spec1d_XSHOO.2018-11-08T00:11:54.072-Feige110_XShooter_VIS_2018Nov08T001154.072.fits',
            'spec1d_XSHOO.2018-11-08T00:11:54.072-Feige110_XShooter_VIS_2018Nov08T001154.072.fits',
            'spec1d_XSHOO.2018-11-12T00:04:37.190-LTT7987_XShooter_VIS_2018Nov12T000437.190.fits',
            'spec1d_XSHOO.2018-11-12T00:04:37.190-LTT7987_XShooter_VIS_2018Nov12T000437.190.fits']
z_qso = 6.51
tell_method = 'qso'
#fileroots = ['J0439_XShooter_VIS_2018Oct09','J0439_XShooter_VIS_2018Oct14','J0439_XShooter_VIS_2018Oct15T',
#             'J0439_XShooter_VIS_2018Oct16','J0439_XShooter_VIS_2018Nov01','J0439_XShooter_VIS_2018Nov08',
#             'J0439_XShooter_VIS_2018Nov09','J0439_XShooter_VIS_2018Nov10','J0439_XShooter_VIS_2018Nov11',
#             'J0439_XShooter_VIS_2018Nov12']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)


## J1120+0641
sci_path = '/d2/Feige/Dropbox/OBS_DATA/XSHOOTER/J1120+0641/VIS/Science'
stdfiles = ['spec1d_XSHOO.2011-02-24T00:13:08.924-LTT3218_XShooter_VIS_2011Feb24T001308.924.fits',
            'spec1d_XSHOO.2011-04-24T23:00:53.399-LTT3218_XShooter_VIS_2011Apr24T230053.399.fits',
            'spec1d_XSHOO.2013-01-24T00:23:29.884-LTT3218_XShooter_VIS_2013Jan24T002329.884.fits',
            'spec1d_XSHOO.2013-01-25T09:33:44.664-GD153_XShooter_VIS_2013Jan25T093344.664.fits',
            'spec1d_XSHOO.2014-02-08T00:34:52.540-GD71_XShooter_VIS_2014Feb08T003452.539.fits',
            'spec1d_XSHOO.2014-02-09T00:26:09.589-GD71_XShooter_VIS_2014Feb09T002609.589.fits',
            'spec1d_XSHOO.2014-02-10T08:24:54.861-GD153_XShooter_VIS_2014Feb10T082454.861.fits',
            'spec1d_XSHOO.2014-02-11T00:36:55.884-GD71_XShooter_VIS_2014Feb11T003655.883.fits',
            'spec1d_XSHOO.2014-02-12T02:50:39.794-GD71_XShooter_VIS_2014Feb12T025039.794.fits',
            'spec1d_XSHOO.2014-02-13T07:42:04.647-GD153_XShooter_VIS_2014Feb13T074204.647.fits',
            'spec1d_XSHOO.2014-02-14T00:35:42.703-GD71_XShooter_VIS_2014Feb14T003542.703.fits',
            'spec1d_XSHOO.2014-02-19T02:10:53.623-LTT3218_XShooter_VIS_2014Feb19T021053.624.fits',
            'spec1d_XSHOO.2014-02-20T00:20:22.815-GD71_XShooter_VIS_2014Feb20T002022.815.fits']
#for ii in range(len(stdfiles)):
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, do_sens=True, do_flux=False, do_stack=False, do_tell=False,
#              disp=False, debug=False)
z_qso = 7.085
tell_method = 'qso'
## Combine everything in one shot
#stdfiles = ['spec1d_XSHOO.2011-02-24T00:13:08.924-LTT3218_XShooter_VIS_2011Feb24T001308.924.fits']
#fileroots = ['J1120+0641_XShooter_VIS']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)
## Combine year by year
#stdfiles = ['spec1d_XSHOO.2011-02-24T00:13:08.924-LTT3218_XShooter_VIS_2011Feb24T001308.924.fits',
#            'spec1d_XSHOO.2013-01-24T00:23:29.884-LTT3218_XShooter_VIS_2013Jan24T002329.884.fits',
#            'spec1d_XSHOO.2014-02-12T02:50:39.794-GD71_XShooter_VIS_2014Feb12T025039.794.fits']
#fileroots = ['J1120+0641_XShooter_VIS_2011','J1120+0641_XShooter_VIS_2013','J1120+0641_XShooter_VIS_2014']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=True, debug=False)



### sensfunction for NIR arm
instrument = 'XSHOOTER_NIR'


## J0439+1634
sci_path = '/d2/Feige/Dropbox/OBS_DATA/XSHOOTER/J0439+1634/reduced/NIR/Science'
stdfiles = ['spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-13T23:56:03.420-LTT7987_XShooter_NIR_2018Oct13T235603.420.fits',
            'spec1d_XSHOO.2018-10-14T23:26:23.121-LTT7987_XShooter_NIR_2018Oct14T232623.121.fits',
            'spec1d_XSHOO.2018-11-08T00:16:56.583-Feige110_XShooter_NIR_2018Nov08T001656.583.fits'
            # Bad 'spec1d_XSHOO.2018-11-12T00:04:40.420-LTT7987_XShooter_NIR_2018Nov12T000440.420.fits'
            # Bad 'spec1d_XSHOO.2018-10-14T23:32:13.290-LTT7987_XShooter_NIR_2018Oct14T233213.290.fits',
            # Bad 'spec1d_XSHOO.2018-10-28T23:47:30.882-LTT7987_XShooter_NIR_2018Oct28T234730.882.fits',
            # Bad 'spec1d_XSHOO.2018-10-28T23:53:20.384-LTT7987_XShooter_NIR_2018Oct28T235320.384.fits',
            # Bad 'spec1d_XSHOO.2018-11-12T00:10:30.590-LTT7987_XShooter_NIR_2018Nov12T001030.590.fits'
            ]
#for ii in range(len(stdfiles)):
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, do_sens=True, do_flux=False, do_stack=False, do_tell=False,
#              disp=False, debug=False)

z_qso = 6.52
tell_method = 'qso'
## Combine everything in one shot
fileroots = ['J0439_XShooter_NIR_2018Oct09','J0439_XShooter_NIR_2018Oct14','J0439_XShooter_NIR_2018Oct15',
             'J0439_XShooter_NIR_2018Oct16','J0439_XShooter_NIR_2018Nov01','J0439_XShooter_NIR_2018Nov08',
             'J0439_XShooter_NIR_2018Nov09','J0439_XShooter_NIR_2018Nov10','J0439_XShooter_NIR_2018Nov11',
             'J0439_XShooter_NIR_2018Nov12']
stdfiles = ['spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits',
            'spec1d_XSHOO.2018-10-08T23:48:26.908-LTT7987_XShooter_NIR_2018Oct08T234826.908.fits']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## J1120+0641
sci_path = '/d2/Feige/Dropbox/OBS_DATA/XSHOOTER/J1120+0641/NIR/Science'
stdfiles = ['spec1d_XSHOO.2013-01-24T00:29:21.509-LTT3218_XShooter_NIR_2013Jan24T002921.509.fits',
            'spec1d_XSHOO.2014-02-19T02:16:45.565-LTT3218_XShooter_NIR_2014Feb19T021645.565.fits']
            ## BAD 'spec1d_XSHOO.2014-02-09T00:26:12.470-GD71_XShooter_NIR_2014Feb09T002612.470.fits',
            ## BAD 'spec1d_XSHOO.2014-02-09T00:39:14.806-GD71_XShooter_NIR_2014Feb09T003914.806.fits',
            ## BAD 'spec1d_XSHOO.2014-02-10T08:37:49.955-GD153_XShooter_NIR_2014Feb10T083749.955.fits',
            ## BAD 'spec1d_XSHOO.2014-02-11T00:49:51.921-GD71_XShooter_NIR_2014Feb11T004951.921.fits',
            ## BAD 'spec1d_XSHOO.2014-02-14T00:48:38.460-GD71_XShooter_NIR_2014Feb14T004838.460.fits',
            ## BAD 'spec1d_XSHOO.2014-02-20T00:33:18.922-GD71_XShooter_NIR_2014Feb20T003318.922.fits']
#for ii in range(len(stdfiles)):
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, do_sens=True, do_flux=False, do_stack=False, do_tell=False,
#              disp=False, debug=False)
z_qso = 7.085
tell_method = 'qso'
## Combine everything in one shot
#stdfiles = ['spec1d_XSHOO.2014-02-19T02:16:45.565-LTT3218_XShooter_NIR_2014Feb19T021645.565.fits']
stdfile = 'spec1d_XSHOO.2013-01-24T00:29:21.509-LTT3218_XShooter_NIR_2013Jan24T002921.509.fits'
fileroot = 'J1120_XShooter_NIR'

flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=False)
## Combine data year by year
#stdfiles = ['spec1d_XSHOO.2013-01-24T00:29:21.509-LTT3218_XShooter_NIR_2013Jan24T002921.509.fits',
#            'spec1d_XSHOO.2013-01-24T00:29:21.509-LTT3218_XShooter_NIR_2013Jan24T002921.509.fits',
#            'spec1d_XSHOO.2014-02-19T02:16:45.565-LTT3218_XShooter_NIR_2014Feb19T021645.565.fits']
#fileroots = ['J1120_XShooter_NIR_2011','J1120_XShooter_NIR_2013','J1120_XShooter_NIR_2014']
#for ii in range(len(fileroots)):
#    fileroot = fileroots[ii]
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#              do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

