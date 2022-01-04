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


Work in progress:

* GitHub Actions workflow: ``.github/workflows/build-site.yaml``

  * build Sphinx docs
    (including Jupyter notebooks)
    and publish rendered docs to ``gh-pages`` branch so that they are visible at
    https://douglatornell.github.io/numeric-refactor/
    whenever commits are pushed to the ``main`` branch


Questions:

* License?
* Copyright notices in files?


Notes:

* I use `Mambaforge`_
  (specifically Mambaforge-pypy3)
  as my conda environment/package manager

.. _Mambaforge: https://github.com/conda-forge/miniforge#mambaforge
