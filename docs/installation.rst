Installation
============

Dependencies
------------

rapidsms-celery-router depends on `django-celery`_. Please follow the django-celery `setup instructions`_ before proceeding with these steps.

.. _django-celery: http://pypi.python.org/pypi/django-celery
.. _setup instructions: http://celery.github.com/celery/django/first-steps-with-django.html

Setup
-----

Install rapidsms-celery-router using Pip_::

    pip install rapidsms-celery-router

This will install the necessary dependencies, including `django-celery`_ and
celery_, if required.

Set ``RAPIDSMS_ROUTER`` in your project's ``settings.py`` to use
``CeleryRouter``::

    RAPIDSMS_ROUTER = "celery_router.router.CeleryRouter"

That's it! Now all incoming and outgoing messages will be queued using Celery.

.. _Pip: http://pip.openplans.org/
.. _celery: http://pypi.python.org/pypi/celery
