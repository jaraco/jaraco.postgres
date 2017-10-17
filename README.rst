.. image:: https://img.shields.io/pypi/v/jaraco.postgres.svg
   :target: https://pypi.org/project/jaraco.postgres

.. image:: https://img.shields.io/pypi/pyversions/jaraco.postgres.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.postgres/master.svg
   :target: http://travis-ci.org/jaraco/jaraco.postgres

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
