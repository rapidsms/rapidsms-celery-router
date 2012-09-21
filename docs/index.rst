.. rapidsms-celery-router documentation master file, created by
   sphinx-quickstart on Thu Sep 20 12:05:59 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to rapidsms-celery-router!
==================================

rapidsms-celery-router is a custom RapidSMS_ router implementation that uses Celery_ to queue incoming and outgoing messages.

.. _RapidSMS: http://www.rapidsms.org/
.. _Celery: http://www.celeryproject.org/

Motivation
----------

RapidSMS ships with a router, ``BlockingRouter``, that processes messages
synchronously in the main HTTP thread. This is fine for most scenarios, but in
some cases you may wish to process messages outside of the HTTP
request/response cycle to be more efficient. rapidsms-celery-router is a custom
router that allows you queue messages for background processing. It's designed
for projects that require high messages volumes and greater concurrency.

Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   configuration
   releases
