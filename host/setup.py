__version__ = '1.0.0.dev0'

import os
import sys
from setuptools import setup, find_packages

DESC = "Renesas (NEC) 78K0 hardware test programs"
here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='k0test',
    version=__version__,
    license='License :: OSI Approved :: BSD License',
    url='https://github.com/mnaberez/k0test',
    description=DESC,
    author="Mike Naberezny",
    author_email="mike@naberezny.com",
    packages=find_packages(),
    install_requires=[
        "k0emu",
        "pyserial",
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'k0test-run = k0test.run:main',
            'k0test-diff = k0test.diff:main',
        ],
    },
)
