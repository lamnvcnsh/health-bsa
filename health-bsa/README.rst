Health-BSA
==========

A small tool to estimate the human body surface area (BSA) from body
weight (kg) and height (cm). This tool support 5 methods

-  Du Bois
-  Mosteller
-  Haycock
-  Gehan and George
-  Fujimoto

Getting started
---------------

The package can be found in the pip.

.. code:: bash

   pip install health-bsa

Usage
-----

This function required two main information: - Body weight (kg) - Body
height (cm)

.. code:: python

   >>> from health_bsa import BSA
   >>> BSA(weight=60,height=170)

The default method is **Du Bois**, if you would like to use another
method using **Method** argument.

.. code:: python

   >>> from health_bsa import BSA
   >>> BSA(weight=60,height=100, method="Mosteller")

You might want to change number of digits, you can use digits parameter.

.. code:: python

   >>> from health_bsa import BSA
   >>> BSA(weight=60,height=100, digits=3)

Contribution
------------

Any contributions are welcome.

Author
------

Lam Nguyen
