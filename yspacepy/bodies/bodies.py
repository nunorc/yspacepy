
""" Body related classes. """

from astropy import units as u
from astropy import constants as const

class Body:
    """ A class for representing a generic astronomical body.

    Args:
        name: object name
        mass: object mass (in kg)
        radisu: object raidus (in meters)
        G: optional G constant

    Returns:
        body: instance of Body
    """
    def __init__(self, name='', mass=0.0 * u.kg, radius=0.0 * u.m, G = const.G):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.mu = G * self.mass

    def __str__(self):
        return self._to_string()

    def __repr__(self):
        return f"Body({ self._to_string() })"

    def _to_string(self):
        return f"name='{ self.name }', mass={ self.mass }, radius={ self.radius }, mu={ self.mu }"
