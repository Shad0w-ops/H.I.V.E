#!/usr/bin/python3
import setuptools
from distutils.core import setup
from os import path
import os

os.system("sudo apt install libimage-exiftool-perl")
os.system("pip3 install -r requirements.txt")
os.system("bash Extras/kali-anonsurf/installer.sh")
os.system("sudo apt install macchanger")

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='intelx',
      version='0.5',
      description='IntelX is a Python command-line utility and API wrapper for intelx.io, made to perform any kind of open-source intelligence.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Kleissner Investments s.r.o./ Dominik Penner',
      author_email='info@intelx.io',
      keywords='intelx intelligence x intelx.io _IntelligenceX IntelligenceX _intelx',
      url='https://github.com/IntelligenceX/SDK/Python',
      packages=['.'],
      scripts=['cli/intelx.py'],
      install_requires=['requests', 'pygments', 'termcolor', 'tabulate']
     )