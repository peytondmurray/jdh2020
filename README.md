# John D Hunter Excellence in Plotting 2020

This repository contains my submission for the John D Hunter Excellence in
Plotting 2020 contest. Inside there are files related to the simulation that
I carried out, the rendering of the animation which is my submission, and
some supporting material.

* `jdh.mx3`: This is the configuration file for the [Mumax3][mumax]
  micromagnetic simulator that I used to simulate the domain wall motion. It
  contains material parameters derived from work that was done at Tampere
  University in a study of domain wall motion and Barkhausen noise in
  disordered magnetic materials.
* `xy.png`: This is a set of axes used in the animation before the simulation
  begins. In the animation, it is used to indicate the size of the simulated
  film.
* `preprocess.py`: This script converts the binary `.ovf` files generated by
  mumax to a single numpy array, and stores the array in a `.npy` file, which
  is faster to load into blender.
* `populate_cones.py`
* `flip_cones.py`
* `demo_rotate.py`
