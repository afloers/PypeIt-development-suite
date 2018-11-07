

import numpy as np
# Read in a wavelength solution and compute
from pypeit import wavecalib
from pypeit.core.wavecal import waveio
from pypeit.core.wavecal import wvutils
from pypeit import utils
from astropy import table
from pypeit import msgs
from matplotlib import pyplot as plt

calibfile ='/Users/joe/python/PypeIt-development-suite/REDUX_OUT/Keck_NIRES/NIRES/MF_keck_nires/MasterWaveCalib_A_01_aa.json'
wv_calib, par = wavecalib.load_wv_calib(calibfile)
steps= wv_calib.pop('steps')
par_dum = wv_calib.pop('par')

datafile ='/Users/joe/python/PypeIt-development-suite/REDUX_OUT/Keck_NIRES/NIRES/MF_keck_nires/MasterWaveCalib_A_01_ac.json'
wv_calib_data, par = wavecalib.load_wv_calib(datafile)
steps= wv_calib_data.pop('steps')
par_dum = wv_calib_data.pop('par')
nslits = len(wv_calib_data)
# assignments
spec = np.zeros((wv_calib_data['0']['spec'].size, nslits))
for slit in range(nslits):
    spec[:,slit] = wv_calib_data[str(slit)]['spec']

nonlinear_counts=par['nonlinear_counts']
sigdetect = par['lowest_nsig']
detections = None
# assignments
lamps = par['lamps']
use_unknowns=True
debug = True
cc_thresh = 0.8
# def archive_reidentify(spec, wv_calib, lamps, detections = None, cc_thresh = 0.8
# rms_threshold = 0.15, nonlinear_counts =par['nonlinear_counts'], sigdetect = par['lowest_nsig'], use_unknowns=True, debug=True)

#

# Generate the line list
line_lists = waveio.load_line_lists(lamps)
unknwns = waveio.load_unknown_list(lamps)
if use_unknowns:
    tot_list = table.vstack([line_lists, unknwns])
else:
    tot_list = line_lists
# Generate the final linelist and sort
wvdata = np.array(tot_list['wave'].data)  # Removes mask if any
wvdata.sort()

nspec = spec.shape[0]
narxiv = len(wv_calib)
nspec_arxiv = wv_calib['0']['spec'].size
if nspec_arxiv != nspec:
    msgs.error('Different spectral binning is not supported yet but it will be soon')

# If the detections were not passed in find the lines in each spectrum
if detections is None:
    detections = {}
    for islit in range(nslits):
        tcent, ecent, cut_tcent, icut = wvutils.arc_lines_from_spec(spec[:, islit], min_nsig=sigdetect,nonlinear_counts=nonlinear_counts)
        detections[str(islit)] = [tcent[icut].copy(), ecent[icut].copy()]
else:
    if len(detections) != nslits:
        msgs.error('Detections must be a dictionary with nslit elements')

# For convenience pull out all the spectra from the wv_calib archive
spec_arxiv = np.zeros((nspec, narxiv))
wave_soln_arxiv = np.zeros((nspec, narxiv))
wvc_arxiv = np.zeros(narxiv, dtype=float)
disp_arxiv = np.zeros(narxiv, dtype=float)
xrng = np.arange(nspec_arxiv)
for iarxiv in range(narxiv):
    spec_arxiv[:,iarxiv] = wv_calib[str(iarxiv)]['spec']
    fitc = wv_calib[str(iarxiv)]['fitc']
    xfit = xrng/(nspec_arxiv - 1)
    fitfunc = wv_calib[str(iarxiv)]['function']
    fmin, fmax = wv_calib[str(iarxiv)]['fmin'],wv_calib[str(iarxiv)]['fmax']
    wave_soln_arxiv[:,iarxiv] = utils.func_val(fitc, xfit, fitfunc, minv=fmin, maxv=fmax)
    wvc_arxiv[iarxiv] = wave_soln_arxiv[nspec_arxiv//2, iarxiv]
    disp_arxiv[iarxiv] = np.median(wave_soln_arxiv[:,iarxiv] - np.roll(wave_soln_arxiv[:,iarxiv], 1))


# Loop over the slits in the spectrum and cross-correlate each with each arxiv spectrum to identify lines
for islit in range(nslits):
    slit_det = detections[str(islit)][0]
    lindex = np.array([], dtype=np.int)
    dindex = np.array([], dtype=np.int)
    wcen = np.zeros(narxiv)
    disp = np.zeros(narxiv)
    shift_vec = np.zeros(narxiv)
    stretch_vec = np.zeros(narxiv)
    ccorr_vec = np.zeros(narxiv)
    for iarxiv in range(narxiv):
        msgs.info('Cross-correlating slit # {:d}'.format(islit + 1) + ' with arxiv slit # {:d}'.format(iarxiv + 1))
        # Match the peaks between the two spectra. This code attempts to compute the stretch if cc > cc_thresh
        success, shift_vec[iarxiv], stretch_vec[iarxiv], ccorr_vec[iarxiv], _, _ = \
            wvutils.xcorr_shift_stretch(spec[:, islit], spec_arxiv[:, iarxiv], cc_thresh=cc_thresh)
        # If cc < cc_thresh or if this optimization failed, don't reidentify from this arxiv spectrum
        if success != 1:
            continue
        # Estimate wcen and disp for this slit based on its shift/stretch relative to the archive slit
        disp[iarxiv] = disp_arxiv[iarxiv] / stretch_vec[iarxiv]
        wcen[iarxiv] = wvc_arxiv[iarxiv] - shift_vec[iarxiv]*disp[iarxiv]
        # For each peak in the arxiv spectrum, identify the corresponding peaks in the input islit spectrum. Do this by
        # transforming these arxiv slit line pixel locations into the (shifted and stretched) input islit spectrum frame
        arxiv_det = wv_calib[str(iarxiv)]['xfit']
        arxiv_det_ss = arxiv_det*stretch_vec[iarxiv] + shift_vec[iarxiv]
        if debug:
            plt.figure(figsize=(14, 6))
            tampl_slit = np.interp(slit_det, xrng, spec[:, islit])
            plt.plot(xrng, spec[:, islit], color='red', drawstyle='steps-mid', label='input arc',linewidth=1.0, zorder=10)
            plt.plot(slit_det, tampl_slit, 'r.', markersize=10.0, label='input arc lines', zorder=10)
            tampl_arxiv = np.interp(arxiv_det, xrng, spec_arxiv[:, iarxiv])
            plt.plot(xrng, spec_arxiv[:, iarxiv], color='black', drawstyle='steps-mid', linestyle=':',
                     label='arxiv arc', linewidth=0.5)
            plt.plot(arxiv_det, tampl_arxiv, 'k+', markersize=8.0, label='arxiv arc lines')
            spec_arxiv_ss = wvutils.shift_and_stretch(spec_arxiv[:, iarxiv], shift_vec[iarxiv], stretch_vec[iarxiv])
            # tampl_ss = np.interp(gsdet_ss, xrng, gdarc_ss)
            for iline in range(arxiv_det_ss.size):
                plt.plot([arxiv_det[iline], arxiv_det_ss[iline]], [tampl_arxiv[iline], tampl_arxiv[iline]],
                         color='cornflowerblue', linewidth=1.0)
            plt.plot(xrng, spec_arxiv_ss, color='black', drawstyle='steps-mid', label='arxiv arc shift/stretch',linewidth=1.0)
            plt.plot(arxiv_det_ss, tampl_arxiv, 'k.', markersize=10.0, label='predicted arxiv arc lines')
            plt.title(
                'Cross-correlation of input slit # {:d}'.format(islit + 1) + ' and arxiv slit # {:d}'.format(iarxiv + 1) +
                ': ccor = {:5.3f}'.format(ccorr_vec[iarxiv]) +
                ', shift = {:6.1f}'.format(shift_vec[iarxiv]) +
                ', stretch = {:5.4f}'.format(stretch_vec[iarxiv]) +
                ', wv_cen = {:7.1f}'.format(wcen[iarxiv]) +
                ', disp = {:5.3f}'.format(disp[iarxiv]))
            plt.ylim(-5.0, 1.5 *spec[:, islit].max())
            plt.legend()
            plt.show()

            # Loop over the current slit line pixel detections and find the nearest arxiv spectrum line
            for iline in range(slit_det.size):
                pdiff = np.abs(slit_det[iline] - arxiv_det_ss)
                bstpx = np.argmin(pdiff)
                # If a match is found within 2 pixels, consider this a successful match
                if pdiff[bstpx] < 2.0:
                    # Using the arxiv arc wavelength solution, search for the nearest line in the line list
                    bstwv = np.abs(wvdata - wave_soln_arxiv[bstpx,iarxiv])
                    # This is probably not a good match
                    if bstwv[np.argmin(bstwv)] > 2.0 * disp_arxiv[iarxiv]:
                        continue
                    lindex = np.append(lindex, np.argmin(bstwv))  # index in the line list self._wvdata
                    dindex = np.append(dindex, iline)
