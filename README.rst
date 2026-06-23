================
HydroIsing-2DTExS
================

This repository contains the latest version of the 2D Ising Equation of State
(https://musesframework.io/docs/modules/eos_ising_texs_2d/Index.html), adapted
for hydrodynamic calculations.

The repository bundles four precomputed EoS tables and a lightweight plotting
script for quick inspection of the resulting thermodynamic observables. Three
tables contain a critical point at different locations, and one reference table
does not contain a critical end point.

Common parameters of the inverted EoSs
--------------------------------------

All tabulated EoSs share the same mapping parameters:

- :math:`\alpha_{12} = 90.0`
- :math:`w = 4.25`
- :math:`\rho = 1.0`

The critical-point coordinates :math:`T` and :math:`\mu_B` differ between the
three CEP-containing tables. The fourth table is a reference EoS without CEP.

Repository layout
-----------------

- ``EoSmub400/``, ``EoSmub500/``, ``EoSmub600/``: tabulated inverted EoS data
   with three different critical-point locations.
- ``EoSwithoutCEP/``: reference table without a critical end point.
- ``scripts/plot.py``: example plotting script using ``numpy`` and
   ``matplotlib``.
- ``Teps.png``, ``mubnb.png``, ``chinb.png``: example figures generated from
   the bundled tables.

Quick start
-----------

1. **Clone the repository**

.. code-block:: bash

   git clone https://github.com/poledtomas/HydroIsing-2DTExS
   cd HydroIsing-2DTExS

2. **Create and activate a virtual environment**

.. code-block:: bash

   python3 -m venv --clear venv
   source ./venv/bin/activate
   pip3 install --upgrade pip
   pip3 install -r requirements.txt

3. **Generate the default plot**

.. code-block:: bash

   python3 scripts/plot.py

The default script reads the :math:`\mu_B = 500` MeV table and writes three PNG
figures into the repository root.

What you get
------------

The script produces three diagnostic plots:

- ``Teps.png``: energy density scaled as :math:`\epsilon / T^4` versus
   temperature.
- ``mubnb.png``: baryon chemical potential versus scaled baryon density
   :math:`n_B / T^3`.
- ``chinb.png``: susceptibility :math:`\chi_2 / T^2` versus
   :math:`n_B / T^3`.

These files are useful as a quick sanity check that the tables load correctly
and that the chosen EoS slice has the expected qualitative structure.

Using a different table
-----------------------

The plotting script currently selects a specific input file directly in
``scripts/plot.py``:

.. code-block:: python

    dat = np.loadtxt(".../EoSmub500/invIsing-2DTExSmub500.dat")

To inspect a different dataset, change that path to one of the bundled tables,
for example:

- ``EoSmub400/invIsing-2DTExSmub400.dat``
- ``EoSmub500/invIsing-2DTExSmub500.dat``
- ``EoSmub600/invIsing-2DTExSmub600.dat``
- ``EoSwithoutCEP/invEoSwithoutCP.dat``

If you switch to a table with a different grid shape, also update ``NTt`` and
``Nmbt`` in the script so that ``numpy.reshape`` matches the selected dataset.

Dependencies
------------

The repository only depends on:

- ``numpy``
- ``matplotlib``

Both are listed in ``requirements.txt``.

Requirements
------------

- Python 3.9+ (recommended)
- Dependencies in ``requirements.txt``

Notes
-----

- The example script is intentionally minimal and is best treated as a starting
   point for custom analysis.
- Plot ranges, labels, and the skipped high-temperature slices are configured in
   ``scripts/plot.py``.

