
""" Orbital mechnics plotting functions. """

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_orbits(ops, labels, cb):
    """ Plot a list of orbits

    Arguments:
        ops: a list of OrbitPropagators objects
        labels: a list of labels
        cb: central body, a Body object

    Returns:
        plot: a plot
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # plot central body
    _u, _v = np.mgrid[0:2*np.pi:40j, 0:np.pi:20j]
    _x = cb.radius.value * np.cos(_u)*np.sin(_v)
    _y = cb.radius.value * np.sin(_u)*np.sin(_v)
    _z = cb.radius.value * np.cos(_v)
    ax.plot_surface(_x, _y, _z, cmap='Greys', alpha=0.5)

    # plot trajectories
    i = 0
    colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd',
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']
    lines = []
    for op in ops:
        r = op.rs
        lines.append(ax.plot(r[:, 0], r[:, 1], r[:, 2], label=labels[i], color=colors[i])[0])
        ax.plot([r[0, 0]], [r[0, 1]], [r[0, 2]], 'x', color='k')
        i += 1

    # plot x,y,z vectors
    l = cb.radius.value * 3.  # FIXME
    x, y, z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    u, v, w = [[l, 0, 0], [0, l, 0], [0, 0, l]]
    ax.quiver(x, y, z, u, v, w, color='k', alpha=0.5)

    # use same scale for x,y,z axis
    max_val = 0
    for op in ops:
        curr_max = np.max(np.abs(op.rs))
        if curr_max > max_val:
            max_val = curr_max
    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])

    # set labels
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')

    plt.legend(lines, labels)
    plt.show()

