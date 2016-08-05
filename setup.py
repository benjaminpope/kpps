from numpy.distutils.core import setup, Extension
from numpy.distutils.misc_util import Configuration
import distutils.sysconfig as ds

long_description = 'Kepler Planet Search: code to search transit-like signals from the kepsys-detrended Kepler light curves.'

setup(name='kpps',
      version='0.5',
      description='Kepler planet search toolkit.',
      long_description=long_description,
      author='Hannu Parviainen',
      author_email='hannu.parviainen@physics.ox.ac.uk',
      url='',
      package_dir={'kpps':'src'},
      scripts=['bin/keplersearch'],
      extra_options = ['-fopenmp'],
      packages=['kpps'],
      ext_modules=[Extension('kpps.blsf', ['src/bls.f90'], libraries=['gomp','m'])],
      install_requires=["numpy", "PyTransit", "PyExoTk"],
      license='GPLv2',
      classifiers=[
          "Topic :: Scientific/Engineering",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Developers",
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ]
     )
