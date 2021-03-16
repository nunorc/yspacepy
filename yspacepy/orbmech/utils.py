
import math as m

# orbital elements to position and velocity vectors
def coes2rv(state0, cb, degrees=True, debug=False):
    # semimajor axis, eccentricity, inclination, longitude of ascending node, argument of periapsis, true anomaly
    a, e, i, lan, ap, nu = state0
    mu = cb.mu.value

    if degrees:
        i = np.deg2rad(i)
        lan = np.deg2rad(lan)
        ap = np.deg2rad(ap)
        nu = np.deg2rad(nu)
    
    p = a * (1-e**2)
    r = p / (1+e*np.cos(nu))
    
    r_pf = r * np.array([np.cos(nu), np.sin(nu), 0])
    v_pf = [-np.sqrt(cb.mu.value/p)*np.sin(nu), np.sqrt(cb.mu.value/p)*(e+np.cos(nu)), 0]

    if debug:
        print('r_pf', r_pf)
        print('v_pf', v_pf)

    pf2eci = np.transpose(eci2fp(nu, ap, i))

    r = np.dot(pf2eci, r_pf)
    v = np.dot(pf2eci, v_pf)

    return r, v

def ecc_anomaly(nu, e):
    return 2*m.atan(m.sqrt((1-e)/(1+e))*m.tan(nu/2.0))

def coes2rv_alt(state0, cb, degrees=True, debug=False):
    # semimajor axis, eccentricity, inclination, longitude of ascending node, argument of periapsis, true anomaly
    a, e, i, lan, ap, nu = state0

    if degrees:
        i = np.deg2rad(i)
        lan = np.deg2rad(lan)
        ap = np.deg2rad(ap)
        nu = np.deg2rad(nu)
    
    E = ecc_anomaly(nu, e)

    r_norm = a*(1-e**2)/(1+e*m.cos(nu))

    r_pf = r_norm * np.array([m.cos(nu), m.sin(nu), 0.0])
    v_pf = m.sqrt(cb.mu.value*a)/r_norm*np.array([-m.sin(E), m.cos(E)*m.sqrt(1-e**2), 0.0])

    pf2eci = np.transpose(eci2fp(nu, ap, i))

    r = np.dot(pf2eci, r_pf)
    v = np.dot(pf2eci, v_pf)

    return r, v

# convert Earth Centered Inertial (ECI) to Perifocal Frame
def eci2fp(raan, aop, i):
    r0 = [-m.sin(raan)*m.cos(i)*m.sin(aop)+m.cos(raan)*m.cos(aop), m.cos(raan)*m.cos(i)*m.sin(aop)+m.sin(raan)*m.cos(aop), m.sin(i)*m.sin(aop)]
    r1 = [-m.sin(raan)*m.cos(i)*m.cos(aop)-m.cos(raan)*m.sin(aop), m.cos(raan)*m.cos(i)*m.cos(aop)-m.sin(raan)*m.sin(aop), m.sin(i)*m.cos(aop)]
    r2 = [m.sin(raan)*m.sin(i), -m.cos(raan)*m.sin(i), m.cos(i)]

    return np.array([r0, r1, r2])


# position and velocity vectors to orbital elements
def rv2coes(state, cb, degrees=True, debug=False):
    r, v = np.array(state[0:3]), np.array(state[3:6])

    if debug:
        print(r, v)

    r_norm = np.linalg.norm(r)
    v_norm = np.linalg.norm(v)

    # angularm momentum
    h = np.cross(r, v)
    h_norm = np.linalg.norm(h)

    # eccentricity (e)
    e = ((v_norm**2-cb.mu.value/r_norm)*r - np.dot(r, v)*v )/cb.mu.value
    e_norm = np.linalg.norm(e)

    # inclination (i)
    i = m.acos(h[2]/h_norm)

    # longitude of ascending node (lan)
    N = np.cross([0, 0, 1], h)    # line of nodes
    N_norm = np.linalg.norm(N)
    lan = m.acos(N[0]/N_norm)
    if N[1] < 0:
        lan = 2*np.pi-lan
    
    # argument of perigee (ap)
    ap = m.acos(np.dot(N,e)/N_norm/e_norm)
    if e[2] < 0:
        ap = 2*np.pi-ap

    # true anomaly (nu)
    nu = m.acos(np.dot(e, r)/e_norm/r_norm)
    if np.dot(r, v) < 0:
        nu = 2*np.pi-nu

    # semi-major axis (a)
    a = r_norm*(1+e_norm*m.cos(nu))/(1-e_norm**2)

    if debug:
        print(f"e={ e_norm } a={ a }")
    
    return np.array([a, e_norm, i, lan, ap, nu])