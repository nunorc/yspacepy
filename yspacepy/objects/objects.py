
from astropy import units as u

class Object:

    def __init__(self, props):
        """ Generic representation of an object.

        Attributes:
            props (dict) dictionary of properties: name, mass, radius and distances
            """
        self.name  = props['name']
        self.mass  = props['mass']
        self.radius = props['radius']
        self.dists = props['dists']

    def dist(self, to):
        """ Retrieve distance to another object.

        Args:
            to: another object

        Returns:
            the distance to the object.
            """
        name = to.name.lower()

        if name in self.dists:
            return self.dists[name]
        else:
            return 'n/a'

    def __repr__(self):
         return "<{} r={:.3e}, m={:.3e}>".format(self.name, self.radius, self.mass)

