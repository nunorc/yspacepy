
from astropy import units as u
from astropy import constants as const

class Body:
    def __init__(self, name='', mass=0.0 * u.kg, radius=0.0 * u.m, G = const.G):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.mu = const.G * self.mass

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return f"Body({ self.to_string() })"

    def to_string(self):
        return f"name='{ self.name }', mass={ self.mass }, radius={ self.radius }, mu={ self.mu }"