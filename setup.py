#!/usr/bin/env python3

from setuptools import setup, find_packages
import unittest


setup(
    name="finite",
    author="Patrick Ziegler",
    license="GPLv3",
    version="0.0.1",
    install_requires=[
        "numpy"
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    test_suite="test.find_all"
)
