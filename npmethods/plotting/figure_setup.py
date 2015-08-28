"""Functions to create standardised matplotlib figures."""

__author__ = 'alansanders'

import matplotlib.pyplot as plt
from math import sqrt

golden_mean = (sqrt(5) - 1.0) / 2.0
opt_height = lambda width: golden_mean * width
widths = dict(regular=11, column=8.5, page=17)
aspects = dict(normal=golden_mean, page=2*golden_mean)

# definitions
# cm_per_inch = 2.54
# inches_per_pt = 1.0/72.27


def get_fig_params(style='sans-serif', tex=False, **kwargs):
    """
    Get a dictionary of the standard figure parameters.

    Args:
        style (str): The font style to use in the figure
        tex (bool): Whether to use LaTeX to render the figure
        **kwargs: Arbitrary keyword arguments that are added to or override existing figure
            parameters.

    Returns:
        dict: A dictionary of figure parameters
    """
    fig_params = {  #'backend': 'pdf',
                    'font.size': 10,
                    'axes.labelsize': 10,
                    #'axes.labelpad': 3.0,  # no longer exists
                    'axes.formatter.use_mathtext': True,
                    'axes.formatter.limits': (-3, 4),
                    'xtick.labelsize': 8,
                    'ytick.labelsize': 8,
                    'legend.fontsize': 10,
                    'legend.labelspacing': 0.2,
                    'text.usetex': tex,
                    'svg.fonttype': 'none',  # used to render svg text as text not paths
                    'font.family': style,
                    'font.serif': ['CMU Serif'],  # 'cmr10'],
                    'font.sans-serif': ['CMU Bright', 'CMU Sans Serif'],  #, 'Helvetica'],
                    'mathtext.fontset': 'cm',
                    'axes.linewidth': 0.7,
                    'patch.linewidth': 0.7,
                    #'savefig.dpi': 300,  # removed since it affects the display res.
                    'savefig.format': 'pdf',
                    'savefig.bbox': 'tight',
                    'ps.papersize': 'A4'
    }
    if tex:
        preamble = r'\usepackage{amsmath}'
        if style == 'sans-serif':
            preamble += ' \usepackage{cmbright}'
        fig_params['text.latex.preamble'] = preamble
    for kwarg in kwargs:
        fig_params[kwarg] = kwargs[kwarg]
    return fig_params


def get_figure_size(width='regular', height=None, aspect='normal'):
    """
    Get the figure width and height from preset values.

    Note that if the height and aspect are both specified then the height takes priority.

    Args:
        width (float, str): width of the figure in cm or a preset string
        height (float): height of the figure in cm
        aspect (float): aspect ratio of the figure (height/width)

    Returns:
        tuple: figure size as (width, height)
    """
    # set the figure size - default unit is inches
    if width in widths:
        width = widths[width]
    inches_per_cm = 1. / 2.54
    fig_width = width * inches_per_cm
    if height is None:
        if aspect in aspects:
            aspect = aspects[aspect]
        fig_height = aspect * fig_width
    else:
        fig_height = height * inches_per_cm
    fig_size = (fig_width, fig_height)
    return fig_size


def setup_figure(width='regular', height=None, aspect='normal', style='sans-serif',
                 tex=False, param_kwargs={}, figure_kwargs={}):
    """
    Create a standardised figure.

    Args:
        width (float, str): width of the figure in cm or a preset string
        height (float): height of the figure in cm
        aspect (float): aspect ratio of the figure (height/width)
        style (str): The font style to use in the figure
        tex (bool): Whether to use LaTeX to render the figure
        **param_kwargs: Arbitrary keyword arguments that are added to or override existing figure
            parameters.
        **figure_kwargs: Arbitrary keyword arguments that are passed to figure creation.

    Returns:
        Figure: a matplotlib figure instance
    """
    # set the figure size
    fig_size = get_figure_size(width, height, aspect)
    # set the figure parameters
    fig_params = get_fig_params(style, tex, **param_kwargs)
    plt.rcParams.update(fig_params)
    formatter = plt.ScalarFormatter(useOffset=False, useMathText=True)
    formatter.set_scientific(True)
    fig = plt.figure(figsize=fig_size, tight_layout=True, **figure_kwargs)
    return fig


def setup_figure_rc(width='regular', height=None, aspect=None, style='sans-serif', tex=False,
                    **kwargs):
    """
    Sets the default configuration for all future figures.

    Args:
        width (float, str): width of the figure in cm or a preset string
        height (float): height of the figure in cm
        aspect (float): aspect ratio of the figure (height/width)
        style (str): The font style to use in the figure
        tex (bool): Whether to use LaTeX to render the figure
        **kwargs: Arbitrary keyword arguments that are added to or override existing figure
            parameters.
    """
    fig_size = get_figure_size(width, height, aspect)
    fig_params = get_fig_params(style, tex, **kwargs)
    fig_params['figure.figsize'] = fig_size
    plt.rcParams.update(fig_params)
    formatter = plt.ScalarFormatter(useOffset=False, useMathText=True)
    formatter.set_scientific(True)


if __name__ == '__main__':
    import numpy as np
    x = np.arange(100)
    y = x**2
    fig = setup_figure()
    plt.plot(x, y)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.show()