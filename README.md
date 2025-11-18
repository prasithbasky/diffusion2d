\# murugapy\_diffusion2d



2D diffusion equation solver and snapshot plotter. Refactored from the SciPython example.



\## Overview

This package solves the two-dimensional diffusion equation on a square plate with a hot circular disc in the center. It uses finite difference discretization and plots snapshots of the temperature field at selected times.



\## Usage

```python

from murugapy\_diffusion2d import solve



\# Use defaults

solve()



\# Custom parameters

solve(dx=0.05, dy=0.05, D=4.0)



