# -*- coding: utf-8 -*-

import os
import sys
import setuptools as st

sys.path.append(os.path.join('src'))
import imreg_dft


st.setup(
    name="imreg_dft",
    version=imreg_dft.__version__,
    author=u"Matěj Týč",
    author_email="matej.tyc@gmail.com",
    description=("Image registration procedure based on discrete Fourier"
                 "transform (DFT)"),
    license="BSD",
    url="https://github.com/matejak/imreg_dft",
    package_dir = {'': 'src'},
    packages = st.find_packages('src'),
    entry_points = {
        'console_scripts': [
           'ird = imreg_dft.cli:main',
        ],
    },
    classifiers=[
        "Development Status :: 1 - Beta",
        "Natural Language :: English",
        "Intended Audience :: Scientists",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)