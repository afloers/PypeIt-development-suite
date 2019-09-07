import numpy as np
from dev_flux_tell import flux_tell

#### sensfunction for DEIMOS
instrument = 'DEIMOS'

#### Generate SENSFUNC
## 830G centered at 8100A
## det 03 and 07
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/Feige110/Science'
stdfiles = ['spec1d_d0526_0134-Feige110_DEIMOS_2017May26T145952.051.fits']
#for ii in range(len(stdfiles)):
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, do_sens=True, do_flux=False, do_stack=False, do_tell=False,
#              disp=True, debug=True)

## 830G centered at 8400A
## det 03 and 07
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J036+03/Science'
stdfiles = ['spec1d_d0914_0048-G191B2B_DEIMOS_2017Sep14T152535.155.fits']
#for ii in range(len(stdfiles)):
#    stdfile = stdfiles[ii]
#    flux_tell(sci_path, stdfile, instrument=instrument, do_sens=True, do_flux=False, do_stack=False, do_tell=False,
#              disp=True, debug=True)


#### FLUXING 830G+8100A
std_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/SENSFUNC/'
stdfile = 'spec1d_d0526_0134-Feige110_DEIMOS_2017May26T145952.051.fits'

## FLUXING J159
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J159-02/Science'
fileroot = 'P159_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=True, debug=False)
## Stack the spectra for J159
spec1dfiles = ['spec1d_d0526_0090-mask_P159_DEIMOS_2017May26T054634.752.fits',
               'spec1d_d0526_0090-mask_P159_DEIMOS_2017May26T054634.752.fits',
               'spec1d_d0526_0091-mask_P159_DEIMOS_2017May26T060748.115.fits',
               'spec1d_d0526_0091-mask_P159_DEIMOS_2017May26T060748.115.fits',
               'spec1d_d0526_0092-mask_P159_DEIMOS_2017May26T062856.813.fits',
               'spec1d_d0526_0092-mask_P159_DEIMOS_2017May26T062856.813.fits']
objids = ['SPAT0394-SLIT0000-DET03','SPAT0395-SLIT0000-DET07',
          'SPAT0394-SLIT0000-DET03','SPAT0394-SLIT0000-DET07',
          'SPAT0394-SLIT0000-DET03','SPAT0394-SLIT0000-DET07']
fileroot = 'J1036-0232_DEIMOS_830G_8100'
z_qso = 6.36
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)


## FLUXING J231
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J231-20/Science'
fileroot = 'P231_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=True, debug=False)
## Stack the spectra for J183
spec1dfiles = ['spec1d_d0526_0109-mask_P231_DEIMOS_2017May26T094122.704.fits',
               'spec1d_d0526_0109-mask_P231_DEIMOS_2017May26T094122.704.fits',
               'spec1d_d0526_0110-mask_P231_DEIMOS_2017May26T100233.130.fits',
               'spec1d_d0526_0110-mask_P231_DEIMOS_2017May26T100233.130.fits',
               'spec1d_d0526_0111-mask_P231_DEIMOS_2017May26T102344.765.fits',
               'spec1d_d0526_0111-mask_P231_DEIMOS_2017May26T102344.765.fits',
               'spec1d_DE.20170527.31707-mask_P231_DEIMOS_2017May27T084820.765.fits',
               'spec1d_DE.20170527.31707-mask_P231_DEIMOS_2017May27T084820.765.fits',
               'spec1d_DE.20170527.32978-mask_P231_DEIMOS_2017May27T090930.413.fits',
               'spec1d_DE.20170527.32978-mask_P231_DEIMOS_2017May27T090930.413.fits',
               'spec1d_DE.20170527.34248-mask_P231_DEIMOS_2017May27T093043.344.fits',
               'spec1d_DE.20170527.34248-mask_P231_DEIMOS_2017May27T093043.344.fits',
               'spec1d_DE.20170527.35520-mask_P231_DEIMOS_2017May27T095153.597.fits',
               'spec1d_DE.20170527.35520-mask_P231_DEIMOS_2017May27T095153.597.fits']
objids = ['SPAT1022-SLIT0000-DET02','SPAT1019-SLIT0000-DET06',
          'SPAT1022-SLIT0000-DET02','SPAT1018-SLIT0000-DET06',
          'SPAT1022-SLIT0000-DET02','SPAT1018-SLIT0000-DET06',
          'SPAT1022-SLIT0000-DET02','SPAT1019-SLIT0000-DET06',
          'SPAT1022-SLIT0000-DET02','SPAT1019-SLIT0000-DET06',
          'SPAT1022-SLIT0000-DET02','SPAT1018-SLIT0000-DET06',
          'SPAT1021-SLIT0000-DET02','SPAT1018-SLIT0000-DET06']
fileroot = 'J1526-2050_DEIMOS_830G_8100'
z_qso = 6.58
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)

## FLUXING J261
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J261+19/Science'
fileroot = 'P261_OFF_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=True, debug=False)
## Stack the spectra for J261
spec1dfiles = ['spec1d_d0527_0080-P261_OFF_DEIMOS_2017May27T102635.318.fits',
               'spec1d_d0527_0080-P261_OFF_DEIMOS_2017May27T102635.318.fits',
               'spec1d_d0527_0081-P261_OFF_DEIMOS_2017May27T104746.349.fits',
               'spec1d_d0527_0081-P261_OFF_DEIMOS_2017May27T104746.349.fits',
               'spec1d_d0527_0083-P261_OFF_DEIMOS_2017May27T113608.093.fits',
               'spec1d_d0527_0083-P261_OFF_DEIMOS_2017May27T113608.093.fits',
               'spec1d_d0527_0084-P261_OFF_DEIMOS_2017May27T115718.864.fits',
               'spec1d_d0527_0084-P261_OFF_DEIMOS_2017May27T115718.864.fits',
               'spec1d_d0527_0085-P261_OFF_DEIMOS_2017May27T121830.586.fits',
               'spec1d_d0527_0085-P261_OFF_DEIMOS_2017May27T121830.586.fits']
objids = ['SPAT0764-SLIT0000-DET03','SPAT0764-SLIT0000-DET07',
          'SPAT0763-SLIT0000-DET03','SPAT0765-SLIT0000-DET07',
          'SPAT0758-SLIT0000-DET03','SPAT0758-SLIT0000-DET07',
          'SPAT0758-SLIT0000-DET03','SPAT0758-SLIT0000-DET07',
          'SPAT0757-SLIT0000-DET03','SPAT0758-SLIT0000-DET07']
fileroot = 'J1724+1901_DEIMOS_830G_8100'
z_qso = 6.44
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)


## FLUXING J338
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J338+29/Science'
fileroot = 'P338_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=True, debug=False)
## Stack the spectra for J338
spec1dfiles = ['spec1d_d0527_0088-mask_P338_DEIMOS_2017May27T125412.269.fits',
               'spec1d_d0527_0088-mask_P338_DEIMOS_2017May27T125412.269.fits',
               'spec1d_d0527_0089-mask_P338_DEIMOS_2017May27T131520.707.fits',
               'spec1d_d0527_0089-mask_P338_DEIMOS_2017May27T131520.707.fits',
               'spec1d_d0527_0090-mask_P338_DEIMOS_2017May27T133710.531.fits',
               'spec1d_d0527_0090-mask_P338_DEIMOS_2017May27T133710.531.fits',
               'spec1d_d0527_0091-mask_P338_DEIMOS_2017May27T135820.266.fits',
               'spec1d_d0527_0091-mask_P338_DEIMOS_2017May27T135820.266.fits']
objids = ['SPAT0953-SLIT0000-DET03','SPAT0956-SLIT0000-DET07',
          'SPAT0953-SLIT0000-DET03','SPAT0956-SLIT0000-DET07',
          'SPAT0954-SLIT0000-DET03','SPAT0956-SLIT0000-DET07',
          'SPAT0953-SLIT0000-DET03','SPAT0956-SLIT0000-DET07']
fileroot = 'J2232+2930_DEIMOS_830G_8100'
z_qso = 6.66
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)


#### FLUXING 830G+8400A
std_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/SENSFUNC/'
stdfile = 'spec1d_d0914_0048-G191B2B_DEIMOS_2017Sep14T152535.155.fits'

## FLUXING J006
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J006+39/Science'
fileroot = 'PSOJ006p39_OFF_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)
## Stack the spectra for J006
spec1dfiles = ['spec1d_DE.20170913.44638-PSOJ006p39_OFF_DEIMOS_2017Sep13T122352.685.fits',
               'spec1d_DE.20170913.44638-PSOJ006p39_OFF_DEIMOS_2017Sep13T122352.685.fits',
               'spec1d_DE.20170913.45911-PSOJ006p39_OFF_DEIMOS_2017Sep13T124503.974.fits',
               'spec1d_DE.20170913.45911-PSOJ006p39_OFF_DEIMOS_2017Sep13T124503.974.fits',
               'spec1d_DE.20170913.47190-PSOJ006p39_OFF_DEIMOS_2017Sep13T130624.854.fits',
               'spec1d_DE.20170913.47190-PSOJ006p39_OFF_DEIMOS_2017Sep13T130624.854.fits',
               'spec1d_DE.20170913.48473-PSOJ006p39_OFF_DEIMOS_2017Sep13T132746.339.fits',
               'spec1d_DE.20170913.48473-PSOJ006p39_OFF_DEIMOS_2017Sep13T132746.339.fits',
               'spec1d_DE.20170913.49749-PSOJ006p39_OFF_DEIMOS_2017Sep13T134902.467.fits',
               'spec1d_DE.20170913.49749-PSOJ006p39_OFF_DEIMOS_2017Sep13T134902.467.fits',
               'spec1d_DE.20170913.51041-PSOJ006p39_OFF_DEIMOS_2017Sep13T141035.616.fits',
               'spec1d_DE.20170913.51041-PSOJ006p39_OFF_DEIMOS_2017Sep13T141035.616.fits',
               'spec1d_DE.20170914.36794-PSOJ006p39_OFF_DEIMOS_2017Sep14T101310.070.fits',
               'spec1d_DE.20170914.36794-PSOJ006p39_OFF_DEIMOS_2017Sep14T101310.070.fits',
               'spec1d_DE.20170914.38070-PSOJ006p39_OFF_DEIMOS_2017Sep14T103423.693.fits',
               'spec1d_DE.20170914.38070-PSOJ006p39_OFF_DEIMOS_2017Sep14T103423.693.fits',
               'spec1d_DE.20170914.39348-PSOJ006p39_OFF_DEIMOS_2017Sep14T105541.894.fits',
               'spec1d_DE.20170914.39348-PSOJ006p39_OFF_DEIMOS_2017Sep14T105541.894.fits']
objids = ['SPAT1061-SLIT0000-DET03','SPAT1063-SLIT0000-DET07',
          'SPAT1036-SLIT0000-DET03','SPAT1038-SLIT0000-DET07',
          'SPAT1011-SLIT0000-DET03','SPAT1013-SLIT0000-DET07',
          'SPAT1088-SLIT0000-DET03','SPAT1089-SLIT0000-DET07',
          'SPAT1112-SLIT0000-DET03','SPAT1114-SLIT0000-DET07',
          'SPAT1101-SLIT0000-DET03','SPAT1102-SLIT0000-DET07',
          'SPAT1053-SLIT0000-DET03','SPAT1056-SLIT0000-DET07',
          'SPAT1029-SLIT0000-DET03','SPAT1032-SLIT0000-DET07',
          'SPAT1081-SLIT0000-DET03','SPAT1083-SLIT0000-DET07']
fileroot = 'J0024+3913_DEIMOS_830G_8400'
z_qso = 6.61
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)

## FLUXING J011
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J011+09/Science'
fileroot = 'PSOJ011p09_OFF_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)
## Stack the spectra for J011
spec1dfiles = ['spec1d_DE.20170914.41912-PSOJ011p09_OFF_DEIMOS_2017Sep14T113824.864.fits',
               'spec1d_DE.20170914.41912-PSOJ011p09_OFF_DEIMOS_2017Sep14T113824.864.fits',
               'spec1d_DE.20170914.43183-PSOJ011p09_OFF_DEIMOS_2017Sep14T115936.326.fits',
               'spec1d_DE.20170914.43183-PSOJ011p09_OFF_DEIMOS_2017Sep14T115936.326.fits',
               'spec1d_DE.20170914.44474-PSOJ011p09_OFF_DEIMOS_2017Sep14T122107.747.fits',
               'spec1d_DE.20170914.44474-PSOJ011p09_OFF_DEIMOS_2017Sep14T122107.747.fits']
objids = ['SPAT1053-SLIT0000-DET03','SPAT1055-SLIT0000-DET07',
          'SPAT1027-SLIT0000-DET03','SPAT1030-SLIT0000-DET07',
          'SPAT1077-SLIT0000-DET03','SPAT1079-SLIT0000-DET07']
fileroot = 'J0045+0910_DEIMOS_830G_8400'
z_qso = 6.42
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)

## FLUXING J036
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J036+03/Science'
fileroot = 'PSOJ036p03_OFF_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)
## Stack the spectra for J036
spec1dfiles = ['spec1d_d0914_0042-PSOJ036p03_OFF_DEIMOS_2017Sep14T133713.037.fits',
               'spec1d_d0914_0042-PSOJ036p03_OFF_DEIMOS_2017Sep14T133713.037.fits',
               'spec1d_d0914_0043-PSOJ036p03_OFF_DEIMOS_2017Sep14T135824.240.fits',
               'spec1d_d0914_0043-PSOJ036p03_OFF_DEIMOS_2017Sep14T135824.240.fits',
               'spec1d_d0914_0044-PSOJ036p03_OFF_DEIMOS_2017Sep14T141953.674.fits',
               'spec1d_d0914_0044-PSOJ036p03_OFF_DEIMOS_2017Sep14T141953.674.fits',
               'spec1d_d0914_0045-PSOJ036p03_OFF_DEIMOS_2017Sep14T144107.728.fits',
               'spec1d_d0914_0045-PSOJ036p03_OFF_DEIMOS_2017Sep14T144107.728.fits',
               'spec1d_d0914_0046-PSOJ036p03_OFF_DEIMOS_2017Sep14T150226.707.fits',
               'spec1d_d0914_0046-PSOJ036p03_OFF_DEIMOS_2017Sep14T150226.707.fits']
objids = ['SPAT1063-SLIT0000-DET03','SPAT1066-SLIT0000-DET07',
          'SPAT1038-SLIT0000-DET03','SPAT1040-SLIT0000-DET07',
          'SPAT1012-SLIT0000-DET03','SPAT1014-SLIT0000-DET07',
          'SPAT1087-SLIT0000-DET03','SPAT1090-SLIT0000-DET07',
          'SPAT1113-SLIT0000-DET03','SPAT1115-SLIT0000-DET07']
fileroot = 'J0226+0302_DEIMOS_830G_8400'
z_qso = 6.53
tell_method = 'qso'
#tell_method = 'poly'
# For this particular source, we need *const_weights* in order to get it right since the SNR difference
# between the last exposure and other exposures are pretty different.
hand_scale = np.array([0.9211053521204734,0.9211053521204734,0.9348072668041172,0.9348072668041172,
                       1.0472179386725955,1.0472179386725955,1.1479181030044185,1.1479181030044185,
                       1.0817046745868977,1.0817046745868977])
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],
#          scale_method='hand', hand_scale=hand_scale,const_weights=True,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)

## FLUXING J2102
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J2102-1458/Science'
fileroot = 'J2102m1458_OFF_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)
## Stack the spectra for J2102
spec1dfiles = ['spec1d_d0914_0020-J2102m1458_OFF_DEIMOS_2017Sep14T053515.821.fits',
               'spec1d_d0914_0020-J2102m1458_OFF_DEIMOS_2017Sep14T053515.821.fits',
               'spec1d_d0914_0021-J2102m1458_OFF_DEIMOS_2017Sep14T055716.790.fits',
               'spec1d_d0914_0021-J2102m1458_OFF_DEIMOS_2017Sep14T055716.790.fits',
               'spec1d_d0914_0022-J2102m1458_OFF_DEIMOS_2017Sep14T061827.907.fits',
               'spec1d_d0914_0022-J2102m1458_OFF_DEIMOS_2017Sep14T061827.907.fits',
               'spec1d_d0914_0023-J2102m1458_OFF_DEIMOS_2017Sep14T063944.035.fits',
               'spec1d_d0914_0023-J2102m1458_OFF_DEIMOS_2017Sep14T063944.035.fits',
               'spec1d_d0914_0024-J2102m1458_OFF_DEIMOS_2017Sep14T070055.584.fits',
               'spec1d_d0914_0024-J2102m1458_OFF_DEIMOS_2017Sep14T070055.584.fits',
               'spec1d_d0914_0025-J2102m1458_OFF_DEIMOS_2017Sep14T072213.008.fits',
               'spec1d_d0914_0025-J2102m1458_OFF_DEIMOS_2017Sep14T072213.008.fits',
               'spec1d_d0914_0026-J2102m1458_OFF_DEIMOS_2017Sep14T074324.298.fits',
               'spec1d_d0914_0026-J2102m1458_OFF_DEIMOS_2017Sep14T074324.298.fits',
               'spec1d_d0914_0027-J2102m1458_OFF_DEIMOS_2017Sep14T080436.451.fits',
               'spec1d_d0914_0027-J2102m1458_OFF_DEIMOS_2017Sep14T080436.451.fits',
               'spec1d_d0914_0028-J2102m1458_OFF_DEIMOS_2017Sep14T082549.469.fits',
               'spec1d_d0914_0028-J2102m1458_OFF_DEIMOS_2017Sep14T082549.469.fits']
objids = ['SPAT1051-SLIT0000-DET03','SPAT1052-SLIT0000-DET07',
          'SPAT1026-SLIT0000-DET03','SPAT1027-SLIT0000-DET07',
          'SPAT1000-SLIT0000-DET03','SPAT1001-SLIT0000-DET07',
          'SPAT1076-SLIT0000-DET03','SPAT1077-SLIT0000-DET07',
          'SPAT1102-SLIT0000-DET03','SPAT1103-SLIT0000-DET07',
          'SPAT1088-SLIT0000-DET03','SPAT1090-SLIT0000-DET07',
          'SPAT1064-SLIT0000-DET03','SPAT1065-SLIT0000-DET07',
          'SPAT1038-SLIT0000-DET03','SPAT1039-SLIT0000-DET07',
          'SPAT1011-SLIT0000-DET03','SPAT1013-SLIT0000-DET07']
fileroot = 'J2102-1458_DEIMOS_830G_8400'
z_qso = 6.61
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)

### Observed with 830G centered at 8100 but need the 8400 sensfunc
## FLUXING J183
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J183+05/Science'
fileroot = 'P183_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)
## Stack the spectra for J183
spec1dfiles = ['spec1d_d0526_0099-mask_P183_DEIMOS_2017May26T070923.270.fits',
               'spec1d_d0526_0099-mask_P183_DEIMOS_2017May26T070923.270.fits',
               'spec1d_d0526_0100-mask_P183_DEIMOS_2017May26T073035.510.fits',
               'spec1d_d0526_0100-mask_P183_DEIMOS_2017May26T073035.510.fits',
               'spec1d_d0526_0101-mask_P183_DEIMOS_2017May26T075148.182.fits',
               'spec1d_d0526_0101-mask_P183_DEIMOS_2017May26T075148.182.fits']
objids = ['SPAT1481-SLIT0000-DET02','SPAT1478-SLIT0000-DET06',
          'SPAT1480-SLIT0000-DET02','SPAT1477-SLIT0000-DET06',
          'SPAT1481-SLIT0000-DET02','SPAT1478-SLIT0000-DET06']
fileroot = 'J1212+0505_DEIMOS_830G_8100'
z_qso = 6.44
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0], wave_grid_min = 6500.0,
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)

## FLUXING J323
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J323+12/Science'
fileroot = 'P323_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)
## Stack the spectra for J323
spec1dfiles = ['spec1d_DE.20170526.48345-mask_P323_DEIMOS_2017May26T132538.899.fits',
               'spec1d_DE.20170526.48345-mask_P323_DEIMOS_2017May26T132538.899.fits',
               'spec1d_DE.20170526.49617-mask_P323_DEIMOS_2017May26T134650.362.fits',
               'spec1d_DE.20170526.49617-mask_P323_DEIMOS_2017May26T134650.362.fits',
               'spec1d_DE.20170526.50888-mask_P323_DEIMOS_2017May26T140803.034.fits',
               'spec1d_DE.20170526.50888-mask_P323_DEIMOS_2017May26T140803.034.fits']
objids = ['SPAT1380-SLIT0000-DET02','SPAT1377-SLIT0000-DET06',
          'SPAT1379-SLIT0000-DET02','SPAT1377-SLIT0000-DET06',
          'SPAT1379-SLIT0000-DET02','SPAT1377-SLIT0000-DET06']
fileroot = 'J2132+1217_DEIMOS_830G_8100'
z_qso = 6.59
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)

## FLUXING J1629
sci_path = '/Users/feige/Dropbox/OBS_DATA/DEIMOS/J1629+2407/Science'
fileroot = 'P247_DEIMOS'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot,
#          do_sens=False, do_flux=True, do_stack=False, do_tell=False, disp=False, debug=False)
## Stack the spectra for J1629
spec1dfiles = ['spec1d_d0526_0122-mask_P247_DEIMOS_2017May26T121306.067.fits',
               'spec1d_d0526_0122-mask_P247_DEIMOS_2017May26T121306.067.fits',
               'spec1d_d0526_0123-mask_P247_DEIMOS_2017May26T123417.443.fits',
               'spec1d_d0526_0123-mask_P247_DEIMOS_2017May26T123417.443.fits',
               'spec1d_d0526_0124-mask_P247_DEIMOS_2017May26T125530.115.fits',
               'spec1d_d0526_0124-mask_P247_DEIMOS_2017May26T125530.115.fits']
objids = ['SPAT0748-SLIT0000-DET03','SPAT0750-SLIT0000-DET07',
          'SPAT0748-SLIT0000-DET03','SPAT0750-SLIT0000-DET07',
          'SPAT0749-SLIT0000-DET03','SPAT0750-SLIT0000-DET07']
fileroot = 'J1629+2407_DEIMOS_830G_8100'
z_qso = 6.48
tell_method = 'qso'
#tell_method = 'poly'
#flux_tell(sci_path, stdfile, spec1dfiles=spec1dfiles, std_path=std_path, instrument=instrument,
#          fileroot=fileroot, objids=objids,  z_qso=z_qso, tell_method=tell_method,
#          fit_region_min=[9200.0], fit_region_max=[9900.0],wave_grid_min = 6500.0,
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=False, debug=False)
