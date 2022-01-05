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


Work in progress:

* refactor an example
  (Lab 1)
  of a notebook and supporting scripts,
  images,
  etc. from ``jupytext``-based workflow and multiple directories into ``website/`` tree


Questions
---------

* License?

* Copyright notices in files?

* Project information in website config? presently:

  ::

    project = "Numeric course"
    copyright = "Numeric project"
    author = "Numeric Project"
    version = ""
    release = "0.1"

* Add list updated date to website page footer?

* Stay with the readthedocs theme? Gallery of some alternatives at https://sphinx-themes.org/


Notes
-----

* I use `Mambaforge`_
  (specifically Mambaforge-pypy3)
  as my conda environment/package manager

.. _Mambaforge: https://github.com/conda-forge/miniforge#mambaforge
