__author__ = 'alansanders'

c = 2.99792458e8
h = 6.62606957e-34
e = 1.602176565e-19


def nm_to_eV(wavelength):
    """
    Converts a wavelength from nm into an energy in eV.

    Args:
        wavelength (float): wavelength in nm

    Returns:
        float: energy in eV
    """
    return 1e9*h*c/wavelength/e


def wavenumber_to_nm(wavenumber):
    """
    Converts a wavenumber into a wavelength.

    Args:
        wavenumber (float): wavenumber in cm^-1

    Returns:
        float: wavelength in nm
    """
    wavenumber /= 1e7  # cm^-1 to nm^-1
    wavelength = wavenumber**-1
    return wavelength


def nm_to_wavenumber(wavelength):
    """
    Converts a wavelength into a wavenumber.

    Args:
        wavelength (float): wavelength in nm

    Returns:
        float: wavenumber in cm^-1
    """
    wavenumber = wavelength**-1
    wavenumber *= 1e7  # nm^-1 to cm^-1
    return wavenumber


def wavenumber_shift_to_nm(excitation_wavelength, wavenumber):
    """
    Converts a wavenumber shift from an excitation wavelength into an emission wavelength.

    Args:
        excitation_wavelength (float): excitation wavelength in nm
        wavenumber (float): wavenumber in cm^-1

    Returns:
        float: wavelength in nm
    """
    #wavenumber /= 1e7  # cm^-1 to nm^-1
    #wavelength = (excitation_wavelength**-1 - wavenumber)**-1
    excitation_wavenumber = nm_to_wavenumber(excitation_wavelength)
    emission_wavenumber = excitation_wavenumber - wavenumber
    wavelength = wavenumber_to_nm(emission_wavenumber)
    return wavelength


if __name__ == '__main__':
    print nm_to_eV(600)
    print wavenumber_shift_to_nm(785, 200)