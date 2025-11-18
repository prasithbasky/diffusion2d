import numpy as np
import matplotlib.pyplot as plt

from .output import create_plot, output_plots


def do_timestep(u_nm1, u, D, dt, dx2, dy2):
    u[1:-1, 1:-1] = (
        u_nm1[1:-1, 1:-1] +
        D * dt * (
            (u_nm1[2:, 1:-1] - 2*u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2 +
            (u_nm1[1:-1, 2:] - 2*u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2
        )
    )
    return u.copy(), u


def solve(dx=0.1, dy=0.1, D=4.0):
    # Plate size
    w = h = 10.0

    # Temperatures
    T_cold = 300
    T_hot = 700

    # Mesh points
    nx, ny = int(w / dx), int(h / dy)

    # Time step (stable)
    dx2, dy2 = dx*dx, dy*dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
    print("dt =", dt)

    # Initial fields
    u0 = T_cold * np.ones((nx, ny))
    u = u0.copy()

    # Hot circular region
    r = min(h, w) / 4
    cx, cy = w/2, h/2
    r2 = r*r

    for i in range(nx):
        for j in range(ny):
            p2 = (i*dx - cx)**2 + (j*dy - cy)**2
            if p2 < r2:
                u0[i, j] = T_hot

    nsteps = 101
    output_steps = [0, 10, 50, 100]

    fig = plt.figure()
    fig_counter = 0
    last_im = None  # for colorbar reference

    for n in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)

        if n in output_steps:
            fig_counter += 1
            last_im = create_plot(fig, u, n, dt, T_cold, T_hot, fig_counter)

    output_plots(fig, last_im)


if __name__ == "__main__":
    solve()
