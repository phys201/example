import numpy as np

def scalar(K, f):
    """
    Manually do a discrete convolution of the psf matrix K and the real image
    f.

    Parameters
    ----------
    K: ndarray
        discrete point spread function matrix where second dimension matches
        size of f
    f: float
        real image before convolution with the point spread function

    Returns
    -------
    recorded: float
        recorded image after convolution with the point spread function
    """
    return K*f


def vector(K, f):
    """
    Manually do a discrete convolution of the psf matrix K and the real image
    f.

    Parameters
    ----------
    K: ndarray
        discrete point spread function square matrix where second dimension
        matches size of f
    f: float or ndarray
        real image before convolution with the point spread function

    Returns
    -------
    recorded: float or ndarray
        recorded image after convolution with the point spread function
    """
    raise NotImplementedError
