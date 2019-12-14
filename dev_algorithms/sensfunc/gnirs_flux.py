from flux_coadd_tell import flux_tell, stack_multinight

#### sensfunction for GNIRS
instrument = 'GNIRS'

## GOOD SENSFUNC
std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/SENSFUNC/'
stdfile = 'spec1d_cN20161014S0481-GD71_GNIRS_2016Oct14T152107.457.fits'
star_ra='05:52:27.61'
star_dec='+15:53:13.8'

## Flux Pisco
sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/J1342+0928/Stack_GD71_NewGrid'
tell_method = 'qso'
fileroot = 'Pisco_GNIRS'
z_qso = 7.5
outroot = 'J1342+0928_GNIRS_GD71_NewGrid'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#          outroot=outroot, star_ra=star_ra, star_dec=star_dec, sens_polyorder=8,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)

## Flux J1120+0641
sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/J1120+0641/Stack_GD71_NewGrid'
tell_method = 'qso'
fileroot = 'J1120+0641'
z_qso = 7.08
outroot = 'J1120+0641_GNIRS_GD71_NewGrid'
flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
          outroot=outroot, star_ra=star_ra, star_dec=star_dec, sens_polyorder=6,
          do_sens=False, do_flux=True, do_stack=True, do_tell=True, disp=False, debug=False)

## Flux J2232+2930
sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/J2232+2930/Stack_GD71_NewGrid'
tell_method = 'qso'
fileroot = 'PSO338+29_GNIRS'
z_qso = 6.62
outroot = 'J2232+2930_GNIRS_GD71_NewGrid'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#          outroot=outroot, star_ra=star_ra, star_dec=star_dec, sens_polyorder=8,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)

## Flux J0024+3913
sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/J0024+3913/Stack_GD71_NewGrid'
tell_method = 'qso'
fileroot = 'PSOJ006_GNIRS'
z_qso = 6.62
outroot = 'J0024+3913_GNIRS_GD71_NewGrid'
#flux_tell(sci_path, stdfile, std_path=std_path, instrument=instrument, fileroot=fileroot, z_qso=z_qso, tell_method=tell_method,
#          outroot=outroot, star_ra=star_ra, star_dec=star_dec, sens_polyorder=8,
#          do_sens=False, do_flux=False, do_stack=False, do_tell=True, disp=True, debug=True)


#######################################################################################
#######################################################################################
#######################################################################################
### OLD fluxing

#### Generate SENSFUNC
#std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut160504/Science/'
### Seems BAD in K-band
#stdfile = 'spec1d_N20160504S0231-GD153_GNIRS_2016May04T110652.059.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=True, debug=True)
# Bad Standard
# stdfile = 'spec1d_N20160504S0232-GD153_GNIRS_2016May04T110947.475.fits'

#std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut161014/Science/'
#stdfile = 'spec1d_cN20161014S0481-GD71_GNIRS_2016Oct14T152107.457.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=True, debug=True)

## coadd2d
#std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut161014/Science_coadd/'
#stdfile = 'spec1d_GD71_coadd2d.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=True, debug=True)

sci_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190908_Tdwarf/Science/'
fileroot = 'J0203-0106_GNIRS'
z_qso = 7.0
tell_method = 'poly'
## Wavelength have problem in the redside, thus I cut out at 24800.0
#flux_tell(sci_path, stdfile, std_path=std_path,instrument=instrument, fileroot=fileroot, z_qso=z_qso,
#          tell_method=tell_method, wave_grid_min=None, wave_grid_max=24800.0,polyorder=5,
#          fit_region_min=[14000.0], fit_region_max=[16000.0],
#          do_sens=False, do_flux=False, do_stack=True, do_tell=True, disp=True, debug=True)

## Get sensfunc with A0 star
std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190531/Science/'
stdfile = 'spec1d_N20190531S0007-HIP50459_GNIRS_2019May31T043733.507.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=6.523,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=True, debug=True)
stdfile = 'spec1d_N20190531S0067-HIP56736_GNIRS_2019May31T073323.707.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=True, debug=True)

std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190601/Science/'
stdfile = 'spec1d_N20190601S0171-HIP56736_GNIRS_2019Jun01T074502.552.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=False, debug=False)

std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190602/Science/'
stdfile = 'spec1d_N20190602S0113-HIP56736_GNIRS_2019Jun02T074159.955.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=False, debug=False)

std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190611/Science/'
stdfile = 'spec1d_N20190611S0066-HIP56736_GNIRS_2019Jun11T040455.775.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=False, debug=False)

std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190612/Science/'
stdfile = 'spec1d_N20190612S0042-HIP56736_GNIRS_2019Jun12T030250.192.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=False, debug=False)

std_path = '/Users/feige/Dropbox/OBS_DATA/GNIRS/ut190613/Science/'
stdfile = 'spec1d_N20190613S0087-HIP56736_GNIRS_2019Jun13T021538.575.fits'
#flux_tell(std_path, stdfile, instrument=instrument, sens_polyorder=8, star_type='A0',star_mag=8.78,
#          do_sens=True, do_flux=False, do_stack=False, do_tell=False, disp=False, debug=False)
