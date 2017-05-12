#!/usr/bin/env python3

from distutils.core import setup

setup(name='dobjobs-parser',
      version='0.1.0',
      description='insert department of buildings jobs into postgres',
      author='ziggy',
      author_email='ziggy@elephant-bird.net',
      url='https://github.com/aepyornis/dob-jobs-parser',
      packages=['dobjobs'],
      package_data={'dobjobs': ['*.sql'] }
     )
