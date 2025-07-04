.. image:: https://img.shields.io/pypi/v/jaraco.postgres.svg
   :target: https://pypi.org/project/jaraco.postgres

.. image:: https://img.shields.io/pypi/pyversions/jaraco.postgres.svg

.. image:: https://github.com/jaraco/jaraco.postgres/actions/workflows/main.yml/badge.svg
   :target: https://github.com/jaraco/jaraco.postgres/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. image:: https://readthedocs.org/projects/jaracopostgres/badge/?version=latest
   :target: https://jaracopostgres.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2025-informational
   :target: https://blog.jaraco.com/skeleton

Routines and fixtures for launching and managing
`PostgreSQL <https://postgresql.org>`_ instances.

Pytest Plugin
=============

This library includes a pytest plugin. To enable it, simply
include this library in your test requirements.

Then, in your tests, simply add a ``postgresql_instance``
parameter to your functions.

Instance
--------

The ``postgresql_instance`` is a ``jaraco.postgres.PostgresServer``
instance with ``host`` and ``port`` properties.
