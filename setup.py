#!/usr/bin/env python
# from distutils.core import setup

import uuid

from setuptools import setup, find_packages

from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(req.req) for req in install_reqs]

setup(name="tweepy",
      version='2.2.0+knowsis',
      description="Twitter library for python",
      license="MIT",
      author="Joshua Roesslein",
      author_email="tweepy@googlegroups.com",
      url="http://github.com/tweepy/tweepy",
      install_requires=reqs,
      packages=find_packages(),
      include_package_data=True,
      keywords="twitter library",
      zip_safe=True)
