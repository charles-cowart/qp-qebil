#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The Qiita Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from setuptools import setup


__version__ = '2023.04'

classes = """
    Development Status :: 4 - Beta
    License :: OSI Approved :: BSD License
    Topic :: Scientific/Engineering :: Bio-Informatics
    Topic :: Software Development :: Libraries :: Application Frameworks
    Topic :: Software Development :: Libraries :: Python Modules
    Programming Language :: Python
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: Implementation :: CPython
    Operating System :: POSIX :: Linux
    Operating System :: MacOS :: MacOS X
"""


with open('README.md') as f:
    long_description = f.read()

classifiers = [s.strip() for s in classes.split('\n') if s]

setup(name='qp-qebil',
      version=__version__,
      long_description=long_description,
      license="BSD",
      description='Qiita Plugin: Knight Lab QEBIL Interface',
      author="Qiita development team",
      author_email="qiita.help@gmail.com",
      url='https://github.com/qiita-spots/qp-qebil',
      setup_requires=["cython"],
      test_suite='nose.collector',
      packages=['qp_qebil'],
      scripts=['scripts/configure_qebil', 'scripts/start_qebil'],
      extras_require={'test': ["nose >= 0.10.1", "pep8"]},
      install_requires=['click >= 3.3', 'future', 'pandas',
                        'qiita-files @ https://github.com/'
                        'qiita-spots/qiita-files/archive/master.zip',
                        'qiita_client @ https://github.com/'
                        'qiita-spots/qiita_client/archive/master.zip'],
      dependency_links=[],
      classifiers=classifiers)
