# -*- coding: utf-8 -*-
from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='prodamuspy',
    version='1.0.2',
    maintainer="Daniil Nagikh",
    maintainer_email="dnagikh@gmail.com",
    url="https://github.com/dnagikh/python-prodamus",
    packages=['prodamuspy'],
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
    long_description=long_description,
    long_description_content_type='text/markdown',
)