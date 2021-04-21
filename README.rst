
=============================
SOATO Registry
=============================

.. image:: https://badge.fury.io/py/uzsoato_registry.svg
    :target: https://badge.fury.io/py/uzsoato_registry/

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
        'rest_framework',
        'django_celery_beat',
        'soato',
        ...
    )


Add settings for celery:

.. code-block:: python

   CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"


Add settings for static files:

.. code-block:: python

   STATIC_URL = "/static/"
   STATUC_ROOT = os.path.join(BASE_DIR, "statis")
   MEDIA_URL = "/media/"
   MEDIA_ROOT = os.path.join(BASE_DIR, "media")


Add Tashkent address registry's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
	path('soato/', include('soato.urls', namespace="soato"),
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
