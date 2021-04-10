=====
Usage
=====

To use SOATO Registry in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'soato.apps.SoatoConfig',
        ...
    )

Add SOATO Registry's URL patterns:

.. code-block:: python

    from soato import urls as soato_urls


    urlpatterns = [
        ...
        url(r'^', include(soato_urls)),
        ...
    ]
