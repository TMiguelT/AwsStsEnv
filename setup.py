#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='aws_sts_env',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'aws-sts-env = aws_sts_env:main',
        ]
    }
)
