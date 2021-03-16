
import numpy as np
import math as m
from scipy.integrate import ode

def null_perts():
    return { 'j2': False, 'aero': False, 'n_bodies': [] }

class OrbitPropagator:
    def __init__(self, state0, tspan, dt, cb, coes=True, degrees=True, propagate=True, perts=null_perts()):
        if coes:
            self.r0, self.v0 = coes2rv(state0, cb, degrees)
        else:
            self.r0 = state0[:3]
            self.v0 = state0[3:]
        self.y0 = self.r0.tolist() + self.v0.tolist()  # concat lists

        self.tspan = tspan
        self.dt = dt
        self.cb = cb

        # total number os steps
        self.n_steps = int(np.ceil(self.tspan/self.dt))

        # initialize arrays
        self.ys = np.zeros((self.n_steps, 6))  # matrix number of steps rows and 6 columns
        self.ys[0] = np.array(self.y0)
        self.ts = np.zeros((self.n_steps, 1))
        self.ts[0] = 0
        self.step = 1

        # perturbations
        self.perts = perts

        if propagate:
            self.propagate_orbit()

    def propagate_orbit(self):
        # init ode
        solver = ode(self.diffy_q)
        solver.set_integrator('vode')
        solver.set_initial_value(self.y0, 0)

        # propagate orbit
        while solver.successful() and self.step < self.n_steps:
            solver.integrate(solver.t+self.dt)
            self.ts[self.step] = solver.t
            self.ys[self.step] = solver.y
            self.step += 1

        self.rs = self.ys[:, :3]
        self.vs = self.ys[:, 3:]

    # function to integrate
    def diffy_q(self, t, y):
        rx, ry, rz, vx, vy, vz = y
        r = np.array([rx, ry, rz])

        r_norm = np.linalg.norm(r)

        ax, ay, az = -r*self.cb.mu.value / r_norm**3

        # TODO add j2 perturbation
        if self.perts['j2']:
            pass

        return [vx, vy, vz, ax, ay, az]