import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='rapidsms-celery-router',
    version=__import__('celery_router').__version__,
    author="RapidSMS development community",
    author_email="rapidsms@googlegroups.com",
    maintainer="RapidSMS development community",
    maintainer_email="rapidsms@googlegroups.com",
    url="http://github.com/rapidsms/rapidsms-celery-router",
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    description=u' '.join(__import__('celery_router').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "django-celery",
    ],
    long_description=read_file('README.rst'),
    tests_require=['mock', ],
    test_suite="runtests.runtests",
    zip_safe=False,
)
