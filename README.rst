================
HydroIsing-2DTExS
================

This repository contains the latest version of the 2D Ising Equation of State
(https://musesframework.io/docs/modules/eos_ising_texs_2d/Index.html), adapted
for hydrodynamic calculations.

Key parameters of the inverted EoS
----------------------------------

- :math:`T_c = 133.356` MeV
- :math:`mu_B = 400.0` MeV
- :math:`alpha_{12} = 90.0`
- :math:`w = 4.25`
- :math:`rho = 1.0`

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

What you get
------------

The script produces the default visualization of the 2D Ising EoS as configured
in ``scripts/plot.py``. Modify that file to adjust ranges, resolution, or plot
style.

Requirements
------------

- Python 3.9+ (recommended)
- Dependencies in ``requirements.txt``

