Configuration
=============

Eager backends
--------------

Sometimes your project may require the use of a synchronous backend. If this is
the case, you can configure specific backends to utilize Celery's eager
functionality with the ``celery_router.eager`` backend setting. For example,
here's how you can force the httptester backend to be eager::

    INSTALLED_BACKENDS = {
        "message_tester": {
            "ENGINE": "rapidsms.contrib.httptester.backend",
            "celery_router.eager": True, # <----------
        },
    }

Using this setting means that the task will be executed in the current process,
and not by an asynchronous worker. Please see the Celery documentation for more
information on `calling tasks`_.

.. _calling tasks: http://celery.github.com/celery/userguide/calling.html#basics

Logging
-------

.. note::

    Please see the `Django logging documentation`_ for further information
    regarding general logging configuration.

All logging specific to rapidsms-celery-router is handled through the
``celery_router`` name. For example, if you have a ``file`` handler defined, you can capture all messages using the following configuration::

    LOGGING_CONFIG = {
        'celery_router': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }

Currently, there are only two child loggers: one for the router and one for the
Celery task. You can capture their messages independently like so::

    LOGGING_CONFIG = {
        'celery_router.router': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'celery_router.tasks.rapidsms_handle_message': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }


.. _Django logging documentation: https://docs.djangoproject.com/en/dev/topics/logging/

BlockingRouter
**************

rapidsms-celery-router's tasks use the ``BlockingRouter`` to route messages. If
you want to capture all router messages, make sure to add, in addition to the
``celery_router`` loggers, ``blockingrouter``::

    LOGGING_CONFIG = {
        'blockingrouter': {
            'handlers': ['file'],
            'level': 'DEBUG',
        }
    }
