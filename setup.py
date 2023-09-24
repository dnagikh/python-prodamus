# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='pyprodamus',
    version='1.0.1',
    maintainer="Daniil Nagikh",
    maintainer_email="dnagikh@gmail.com",
    url="https://github.com/dnagikh/pyprodamus",
    packages=['pyprodamus'],
    install_requires=[],
    license='LICENSE.md',
    description='Prodamus hash verifier',
    keywords=["prodamus", "hash", "hmac", "verify", "sign"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security :: Cryptography",
        ],
    long_description=open('README.md').read(),
)