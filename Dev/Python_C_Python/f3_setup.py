# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("f1_sum_numbers.pyx")
)
