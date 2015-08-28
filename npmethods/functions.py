__author__ = 'alansanders'

import numpy as np


gaussian = lambda x, x0, sigma, a: a * np.exp(-(x-x0)**2/(2*sigma**2))  # * (1./(sigma*np.sqrt(2*np.pi)))
lorentzian = lambda x, x0, gamma, a: a * 1./np.pi * (gamma/2.) / ((x-x0)**2 + (gamma/2.)**2)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    x = np.linspace(-1, 1, 100)
    y = gaussian(x, 0, 1, 1)
    plt.plot(x, y)
    plt.show()