
from astropy import units as u
from .bodies import Body

# sun
sun = Body(name='Sun', mass=1.989e30 * u.kg, radius=696340e3 * u.m)

# earth
earth = Body(name='Earth', mass=5.972e24 * u.kg, radius=6.371e6 * u.m)

# moon
moon = Body(name='Moon', mass=7.34767309e22 * u.kg, radius=1737e3 * u.m)

# jupiter
jupiter = Body(name='Jupiter', mass=1.898e27 * u.kg, radius=69911e3 * u.m)

# neptune
neptune = Body(name='Neptune', mass=1.024e26 * u.kg, radius=24622 * u.km)
