__author__ = 'alansanders'

from matplotlib.colors import LinearSegmentedColormap

_cmap_data = {'red': ((0., 0, 0),
                      (0.25, 0, 0),
                      (0.55, 1, 1),
                      (0.85, 1, 1),
                      (1, 0.6, 0.6)),
              'green': ((0., 0.2, 0.2),
                        (0.1, 0.4, 0.4),
                        (0.45, 1, 1),
                        (0.55, 1, 1),
                        # (0.8, 0, 0),
                        (0.85, 0, 0),
                        (1, 0., 0.)),
              'blue': ((0., 0.5, 0.5),
                       (0.2, 1, 1),
                       (0.85, 0, 0),
                       (0.85, 0, 0),
                       (1, 0., 0.))
}

np_cmap = LinearSegmentedColormap('np_cmap', _cmap_data, 256)