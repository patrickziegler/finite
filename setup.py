#!/usr/bin/env python3

from setuptools import setup, find_packages


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
    test_suite="tests"
)
