# Background
On nanometer length scales, ferromagnetic materials are made up of microscopic magnetic moments, with each moment producing its own magnetic field. When a large number of moments align to form _domains_ of parallel magnetization, producing a macroscopic field which is readily observed in the attraction (and repulsion) between everyday bar magnets. This phenomenon, known as ferromagnetism, has wide ranging technological applications, with ferromagnetic materials playing central roles in electric motors and generators, data storage, and sensors. Understanding the behavior of these materials on the microscopic level is therefore critical for next-generation device applications.

While understanding the dynamical behavior of magnetic moments themselves is important for technological applications, more recently the boundaries _between_ magnetic domains, known as _domain walls_, have also attracted attention. The animation presented here focuses on one such _domain wall_, and depicts the simulated motion of magnetic moments in a layer of disordered magnetic material $0.5\;\mathrm{nm}$ thick and $512 \times 1024\;\mathrm{nm}^2$ in area. The thin film was intialized with the moments along the left side of the film pointing along $-\hat{z}$, and those along the right side of the film pointing along $+\hat{z}$. A magnetic field of $\vec{H} = 100 Oe$ was applied along $-\hat{z}$, and the system was allowed to evolve in time according to the [Landau-Lifshitz-Gilbert][llg] (LLG) equation, with periodic boundary conditions applied in the $y$-direction. Integration of the LLG equation was carried out using a finite differences scheme using the [Mumax3][mumax] micromagnetic solver.


Realistic material parameters were chosen for the simulation based on research

Additional details of the micromagnetic parameters used for the simulation can be found in the [repository] for this project.







* Matplotlib's `RdBu` colormap was used to color the $z$-component of the magnetization, with $-\hat{z}$ (down) mapped to red, and $+\hat{z}$ (up) mapped to blue.

# Impact
In ferromagnetic materials, [exchange][exchange], [dipolar][dipolar], [Zeeman][zeeman], and [magnetocrystalline anisotropy][anisotropy] compete on similar energy scales, giving rise to complicated collective behavior.









[exchange]: https://en.wikipedia.org/wiki/Exchange_interaction
[dipolar]: https://en.wikipedia.org/wiki/Exchange_interaction
[zeeman]: https://en.wikipedia.org/wiki/Exchange_interaction
[anisotropy]: https://en.wikipedia.org/wiki/Exchange_interaction
[mumax]: https://github.com/mumax/3
