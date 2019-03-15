# -*- coding: utf-8 -*-
"""
@author: Jussi (jnu@iki.fi)
"""

from setuptools import setup, find_packages


setup(name='liikelaaj',
      version='0.10',
      description='Input and report movement range data',
      author='Jussi Nurminen',
      author_email='jnu@iki.fi',
      license='GPLv3',
      url='https://github.com/jjnurminen/liikelaaj',
      packages=find_packages(),
      entry_points={
              'console_scripts': ['liikelaaj=liikelaaj.liikelaajuus:main']
              },
      include_package_data=True,
      )
