#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup

setup(

    name='Flask-Triangle',
    version='0.1',
    author='Morgan Delahaye-Prat',
    author_email='mdp@arjel.fr',
    description=('Integration of Angular and Flask.'),
    long_description=open('README.rst').read(),
    packages=['flask_triangle'],
    zip_safe=False,
    platforms='any',
    install_requires=['flask', 'jsonschema', 'six'],
    tests_require=['nose'],
    url='https://github.com/morgan-del/flask-triangle',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)