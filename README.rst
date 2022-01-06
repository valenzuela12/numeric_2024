Numeric Course Repo Refactoring Experiment
==========================================

The initial experiment of creating a repo with a single-truth copy of the notebooks
and related modules,
images,
PDFs,
etc. was a success:

* The ``website/`` tree is auto-published to GitHub Pages via an on-push GitHub Actions workflow
  and the ``gh-pages`` branch.

* Instructors can edit the lab notebooks and code modules in the ``notebooks/``
  and ``numlabs/`` trees.

* Students can:

  * fork the repo on GitHub and clone their for to their laptops
  * set up an ``upstream`` remote to allow them to pull updates from the instructor-maintained repo
  * create personally named copies of the lab notebooks to avoid merge conflicts with updates from ``upstream``
  * commit their changes and push them to their GitHub forks

Next steps:

* Pull the rest of the content from ``numeric_2022`` into this repo

* Do the stuff flowing from answers in the Questions section below

* Transfer the "ready enough for day 1" repo to Rachel's ownership on GitHub

* Tidy up notebook rendering and mark-up issues

See https://github.com/users/douglatornell/projects/1/views/4?layout=board for details.


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

* License?

  Susan says:

      Given that it is mostly text in the notebooks, lets go creative commons.
      I'm using: Worksheets for Numeric Course by Susan Allen, Rachel White, Phil Austin
      and The University of British Columbia are licensed under a
      Creative Commons Attribution 3.0 Unported License.
      Feel free to add yourself or refer to a contributors list.

  I suggest Creative Commons Attribution 4.0 International, the updated version of 3.0 Unported

* Copyright notices in files?

  Susan says:

      Yes please, but I'll reach out to Phil to double check.

* Project information in website config? presently:

  ::

    project = "Numeric course"                  Fine
    copyright = "Numeric project"               Change to contributors and add a contributors page?
    author = "Numeric Project"                  Fine
    version = ""                                202201
    release = "0.1"                             what do you suggest?

  I suggest:

  ::

    version = "22.1"
    release = version

  Version follows the ``YY.N`` pattern we use for SalishSeaCast packages that is
  somewhat in line with https://calver.org/ without getting hung up on the month
  in the version;
  ``N`` is just a sequential number that gets incremented when the accumulated changes
  are deemed to be "significant".
  I don't really expect there to be a ``22.2`` version of the course.
  Next will likely be ``24.1``.


* Add list updated date to website page footer?

  Susan says:

      Yes.

* Stay with the readthedocs theme? Gallery of some alternatives at https://sphinx-themes.org/
  Susan says:

    Switch the theme so its clear we are on a new site.  I like Sandstone.

* Is ``numlabs.show_figure`` important? It's not mentioned anywhere in narrative pages or notebooks

  Susan says:

    Probably cruft.


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
