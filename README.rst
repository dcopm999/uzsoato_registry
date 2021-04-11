=============================
SOATO Registry
=============================

.. image:: https://badge.fury.io/py/uzsoato_registry.svg
    :target: https://badge.fury.io/py/uzsoato_registry

.. image:: https://travis-ci.com/dcopm999/uzsoato_registry.svg?branch=master
    :target: https://travis-ci.com/dcopm999/uzsoato_registry

.. image:: https://codecov.io/gh/dcopm999/uzsoato_registry/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/uzsoato_registry

SOATO Registry of Uzbekistan

Documentation
-------------

The full documentation is at https://uzsoato_registry.readthedocs.io.

Quickstart
----------

Install SOATO Registry::

    pip install uzsoato_registry

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'soato',
        ...
    )

Add SOATO Registry's URL patterns:

.. code-block:: python

    from soato import urls as soato_urls


    urlpatterns = [
        ...
        path('', include(soato_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
