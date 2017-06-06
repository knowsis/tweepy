#!/usr/bin/env python
# from distutils.core import setup

import uuid

from setuptools import setup, find_packages
from tweepy.version import version as __version__

from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(req.req) for req in install_reqs]

setup(name="tweepy",
      version=__version__,
      description="Twitter library for python",
      license="MIT",
      author="Joshua Roesslein",
      author_email="tweepy@googlegroups.com",
      url="http://github.com/tweepy/tweepy",
      install_requires=reqs,
      packages=find_packages(),
      keywords="twitter library",
      zip_safe=True)
