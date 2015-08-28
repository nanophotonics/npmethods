"""Functions to plot spectra in a standardised manner."""

__author__ = 'alansanders'

import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d as gf1d


def plot_spectrum(wavelength, spectrum, ax=None, plot_raw=True, smooth=10,
                  raw_kwargs=dict(markersize=1., color='k', linestyle='', marker='.'),
                  **kwargs):
    """
    Standardised method for plotting a spectrum on a matplotlib axes. The raw spectrum is plotted
    as dots and a smoothed line is drawn through.

    Args:
        wavelength (np.ndarray): array of wavelengths
        spectra (np.ndarray): array of spectrum values
        ax (matplotlib.axis): An matplotlib axis instance. If none exist then one will be created
        plot_raw (bool): Plot the raw data as black dots
        smooth (float): sigma for Gaussian smoothing
        raw_kwargs (dict): Dictionary of keyword arguments passed to the axes plot method for the
            raw spectrum plot
        **kwargs: Arbitrary keyword arguments passed to the axes plot method for the smoothed
            spectrum plot
    """
    if ax is None:
        ax = plt.gca()
        if ax is None:
            ax = plt.subplot(111)
    if plot_raw:
        print 'plotting'
        ax.plot(wavelength, spectrum, **raw_kwargs)
    if 'linestyle' not in kwargs:
        kwargs['linestyle'] = '-'
    ax.plot(wavelength, gf1d(spectrum, smooth), **kwargs)


if __name__ == '__main__':
    import numpy as np
    x = np.linspace(400, 800, 1000)
    y = np.exp(-(x-600)**2/50**2) + np.random.normal(0, 0.1, x.size)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plot_spectrum(x, y, ax, smooth=10, raw_kwargs=dict(markersize=2., color='k', linestyle='',
                                                       marker='.'))
    plt.show()
