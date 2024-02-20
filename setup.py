from io import open
from os import path
import sys

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
name = "showcleaner"
description = "Show cleaner (movies, tv shows...)"
version = "0.0.1"
release_status = "Development Status :: 3 - Alpha"
dependencies = [
    'imdbpy'
]
extras = {
    'dev': ['coverage', 'flake8', 'watchdog', 'asciinema-automation'],
    'google': ['google-api-python-client', 'google-auth', 'gspread']
}
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
sys.dont_write_bytecode = True

setup(name=name,
      version=version,
      description=description,
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Olivier Cervello',
      author_email='olivier.cervello@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs']),
      classifiers=[
          release_status,
          'Intended Audience :: Developers',
          'Programming Language :: Python',
      ],
      keywords='recon framework vulnerability pentest automation',
      install_requires=dependencies,
      include_package_data=True,
      extras_require=extras,
      entry_points={
          'console_scripts': ['showcleaner=showcleaner.cli:cli'],
      },
      python_requires='>=3.8')
