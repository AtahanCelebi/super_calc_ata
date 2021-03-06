import setuptools
from setuptools import setup, find_packages
import os

from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="super_calc_hacettepe",                     # This is the name of the package
    version="0.1.0",                        # The initial release version
    author="Atahan Çelebi",                     # Full name of the author
    description="Quicksample HACETTEPE",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),    # List of all python modules to be installed
    
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
                 # Name of the python package
    package_dir={'':'src'},     # Directory of the source code of the package
    install_requires=['pysal >= 2.0.0'],                     # Install other dependencies if any
    package_data={'': ['yazilar.txt'],'super_calc_hacettepe':['test/*']},
    download_url='https://github.com/AtahanCelebi/super_calc_ata/archive/refs/tags/0.1.0.tar.gz',
    url = 'https://github.com/AtahanCelebi/super_calc_ata'
)

