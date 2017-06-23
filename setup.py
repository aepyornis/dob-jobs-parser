#!/usr/bin/env python3
# from distutils.core import setup
from setuptools import setup

setup(name='dobjobs-parser',
      version='0.1.1',
      description='insert department of buildings jobs into postgres',
      author='ziggy',
      author_email='ziggy@elephant-bird.net',
      url='https://github.com/aepyornis/dob-jobs-parser',
      packages=['dobjobs'],
      package_data={'dobjobs': ['*.sql', 'headers.txt'] },
      entry_points={
          'console_scripts': [
              'dobjobs = dobjobs.parse:main',
          ]
      }
     )
