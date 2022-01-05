Numeric Course Repo Refactoring Experiment
==========================================

Features
--------

Completed:

* conda environment: ``envs/environment.yaml``

* `pre-commit`_ hooks: ``.pre-commit-config.yaml``

  * delete trailing whitespace
  * ensure exactly 1 newline at the ends of files
  * ensure that YAML files are parsable
  * prevent commits containing files larger than 500 KB

  .. _pre-commit: https://pre-commit.com/

* a fairly detailed ``.gitignore`` file to try to avoid file that shouldn't be tracked
  finding their way into the repo

* added UBC EOAS favicon for browser tabs and bookmarks

* GitHub Actions workflow: ``.github/workflows/sphinx-to-gh-pages.yaml``

  * build Sphinx website
    and publish its html, etc. to ``gh-pages`` branch so that it is updated at
    https://douglatornell.github.io/numeric-refactor/
    whenever commits are pushed to the ``main`` branch

* refactor an example
  (Lab 1)
  of a notebook and supporting scripts,
  images,
  etc. from ``jupytext``-based workflow and multiple directories into ``website/`` tree


Questions
---------

* License?   Given that it is mostly text in the notebooks, lets go creative commons.  I'm using: Worksheets for Numeric Course by Susan Allen, Rachel White, Phil Austin and The University of British Columbia are licensed under a Creative Commons Attribution 3.0 Unported License.  Feel free to add yourself or refer to a contributors list.

* Copyright notices in files?  Yes please, but I'll reach out to Phil to double check.

* Project information in website config? presently:

  ::

    project = "Numeric course"                  Fine
    copyright = "Numeric project"               Change to contributors and add a contributors page?
    author = "Numeric Project"                  Fine
    version = ""                                202201 
    release = "0.1"                             what do you suggest?

* Add list updated date to website page footer?  Yes.

* Stay with the readthedocs theme? Gallery of some alternatives at https://sphinx-themes.org/   Switch the theme so its clear we are on a new site.  I like Sandstone.

* Is ``numlabs.show_figure`` important? It's not mentioned anywhere in narrative pages or notebooks   Probably cruft.


Notes
-----

* I use `Mambaforge`_
  (specifically Mambaforge-pypy3)
  as my conda environment/package manager

.. _Mambaforge: https://github.com/conda-forge/miniforge#mambaforge

* ``<div>`` tags around display math in notebooks prevent math rendering in VSCode but not
  ``jupyter lab`` or ``jupyter notebook``.
  Removing them fixes rendering in VSCode and doesn't affect ``lab`` or ``notebook`` rendering.

* There are a bunch of other displaymath rendering issues when the notebooks are viewed in VSCode.
  At least some are due to displaymath having text before or after it on the same line;
  easily resolved by adding newlines,
  but tedious...

* Sphinx warns of various markup issues in lab1:

  ::

    reading sources... [100%] notebooks/lab1/01-lab1
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:819: WARNING: Title level inconsistent:

    Example Four
    ^^^^^^^^^^^^
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:829: WARNING: Title level inconsistent:

    Example Five
    ^^^^^^^^^^^^
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:954: WARNING: Title level inconsistent:

    Demo: Interpolation
    ^^^^^^^^^^^^^^^^^^^
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:1086: WARNING: Title level inconsistent:

    Interpolation Quiz
    ^^^^^^^^^^^^^^^^^^
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:1221: WARNING: Title level inconsistent:

    Discretization Quiz
    ^^^^^^^^^^^^^^^^^^^
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:1278: WARNING: Title level inconsistent:

    Summary
    ^^^^^^^
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:1329: WARNING: Title level inconsistent:

    Example Six
    ^^^^^^^^^^^
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:1972: WARNING: Unexpected indentation.
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:1969: WARNING: Inline interpreted text or phrase reference start-string without end-string.
    /media/doug/warehouse/EOAS-teaching/numeric-refactor/website/notebooks/lab1/01-lab1.ipynb:1973: WARNING: Block quote ends without a blank line; unexpected unindent.
