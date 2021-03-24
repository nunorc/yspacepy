
# yspacepy

## Installation

    $ pip install yspacepy

## Astronomical Bodies

```python
>>> from yspacepy.bodies import earth
>>> earth
Body(name='Earth', mass=5.972e+24 kg, radius=6371000.0 m, mu=398589196000000.0 m3 / s2)
>>> earth.radius
<Quantity 6371000. m>
>>> earth.radius.to('km')
<Quantity 6371. km>
>>> earth.radius.to('km').value
6371.0
```

## Orbital Mechanics

Earth orbit around the Sun example.

```python
import numpy as np
from yspacepy.bodies import sun, earth
from yspacepy.orbmech import OrbitPropagator, plot_orbits

# initial conditions of orbital parameters
r_mag = sun.radius.value + 1.496e11
v_mag = 30000

# initial position and velocity vectors
state0 = np.array([r_mag, 0, 0, 0, v_mag, 0])

# timespan
tspan = 3.5e7

# time step
dt = 86400.0

# propagate orbit
sun_earth = OrbitPropagator(state0, tspan, dt, sun, coes=False)

# plot orbit
plot_orbits([sun_earth], labels=['Earth'], cb=sun)# plot orbit
```

ISS low earth orbit around the Earth example.

```python
import numpy as np
from yspacepy.bodies import sun, earth
from yspacepy.orbmech import OrbitPropagator, plot_n_orbits

# initial conditions of orbital parameters
r_mag = earth.radius.value + 4e5
v_mag = np.sqrt(earth.mu.value/r_mag)

# initial position and velocity vectors
state0 = np.array([r_mag, 0, 0, 0, v_mag, 0])

# timespan
tspan = 100 * 60.0

# time step
dt = 100.0

earth_iis = OrbitPropagator(state0, tspan, dt, earth, coes=False)

# plot orbit
plot_orbits([earth_iis], labels=['IIS'], cb=earth)
```