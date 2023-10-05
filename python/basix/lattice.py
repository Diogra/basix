"""Functions to manipulate lattice types."""

from ._basixcpp import LatticeSimplexMethod as _LSM
from ._basixcpp import LatticeType as _LT


def string_to_type(lattice: str) -> _LT:
    """Convert a string to a Basix LatticeType enum.

    Args:
        lattice: Lattice type as a string.

    Returns:
        The lattice type.

    """
    if not hasattr(_LT, lattice):
        raise ValueError(f"Unknown lattice: {lattice}")
    return getattr(_LT, lattice)


def type_to_string(latticetype: _LT) -> str:
    """Convert a Basix LatticeType enum to a string.

    Args:
        latticetype: Lattice type

    Returns:
        The lattice type as a string.

    """
    return latticetype.__name__


def string_to_simplex_method(method: str) -> _LSM:
    """Convert a string to a Basix LatticeSimplexMethod enum.

    Args:
        method: The simplex method as a string.

    Returns:
        The simplex method.

    """
    if not hasattr(_LSM, method):
        raise ValueError(f"Unknown simplex method: {method}")
    return getattr(_LSM, method)


def simplex_method_to_string(simplex_method: _LSM) -> str:
    """Convert a Basix LatticeSimplexMethod enum to a string.

    Args:
        simplex_method: Simplex method.

    Returns:
        The simplex method as a string.

    """
    return simplex_method.__name__
