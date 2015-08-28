__author__ = 'alansanders'

from collections import Sequence
import numpy as np
from scipy.interpolate import interp1d
from scipy.ndimage.filters import gaussian_filter1d as gf1d


def get_roi(a, amin, amax, skip=None):
    """Get a slice of an array in a specified range."""
    return slice(np.min(np.where(a >= amin)), np.max(np.where(a <= amax))+1, skip)


def get_nearest(a, value):
    """Get the value of the array element nearest to the specified value."""
    return abs(a-value).argmin()


def downsample_array(a, skip=1):
    if (a.size % skip) != 0:
        r = a.size % skip
        a = a[:-r]
    return np.mean(a.reshape(-1, skip), axis=1)


def get_closest_multiple(n, m):
    """Get the closest (low) multiple, m, of a number, n."""
    return n - (n % m)


def bin_spectrum(wavelengths, spectrum, bins):
    """
    Average a spectrum across a number of wavelength bands.

    Bin and average a spectrum and its wavelengths.

    Args:
        wavelengths (np.ndarray):
        spectrum (np.ndarray):
        bins (int or sequence): the number of bins to generate or the bin edges as a sequence

    Returns:
        (binned_wavelengths, binned_spectrum) (np.ndarray): the average wavelength and spectrum
        of each wavelength band

    Raises:
        ValueError: if bins is not a 1d array
    """
    if type(bins) == int:
        bins = np.linspace(np.min(wavelengths), np.max(wavelengths), bins)
    elif isinstance(bins, (Sequence, np.ndarray)):
        print 'bins is a sequence'
        if isinstance(bins, Sequence):
            print 'bins is not an array'
            bins = np.array(bins)
        if len(bins.shape) != 1:
            raise ValueError('bins must be 1d')
    digitized = np.digitize(wavelengths, bins, right=False)
    # computation is done in 2 stages to initially preserve the raw binned data if needed
    binned_wavelengths = [wavelengths[np.where(digitized == i+1)] for i in range(len(bins))]
    binned_wavelengths = np.array([np.mean(binned_wavelengths[i]) for i in range(len(binned_wavelengths))])
    binned_spectrum = [spectrum[np.where(digitized == i+1)] for i in range(len(bins))]
    binned_spectrum = np.array([np.mean(binned_spectrum[i]) for i in range(len(binned_spectrum))])
    return binned_wavelengths, binned_spectrum


def interpolate_spectrum(wavelength, spectrum, smooth=10):
    func = interp1d(wavelength, spectrum)
    new_wavelength = np.arange(wavelength.min(), wavelength.max(), 1)
    new_spectrum = func(new_wavelength)
    new_spectrum = gf1d(new_spectrum, smooth)
    return new_wavelength, new_spectrum


def threshold_array(a, threshold):
    """
    Threshold an array, removing the array contents if below the threshold fraction.

    The array below threshold is set to NaN.

    Args:
        a (sequence): the array/sequence/iterable to be thresholded
        threshold (float): the fraction of range of the array data below which is removed

    Returns:
        a (np.ndarray): the thresholded array
    """
    threshold = threshold*np.max(a) + (1 - threshold)*np.min(a)  # n(x-y)+y = nx +y(1-n)
    return np.where(a >= threshold, a, np.nan)


if __name__ == '__main__':
    a = np.arange(-50,50)**2
    a -= 1000
    a = threshold_array(a, 0.1)
    a -= np.min(a[np.isfinite(a)])
    a /= np.max(a[np.isfinite(a)])
    print a