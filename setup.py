#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from setuptools import setup, find_packages


setup(
    name="rapidsms-celery-router",
    version=__import__('timepiece').__version__,
    license="BSD",
    install_requires=[
        "dajngo-celery",
    ],
    packages=find_packages(),
    include_package_data=True,
    author="RapidSMS development community",
    author_email="rapidsms@googlegroups.com",
    maintainer="RapidSMS development community",
    maintainer_email="rapidsms@googlegroups.com",
    description="RapidSMS Router implementation using Celery",
    url="http://github.com/rapidsms/rapidsms-celery-router",
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
)
