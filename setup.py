from setuptools import setup, find_packages
setup(name='map_elites',
      version='0.1',
      packages = find_packages(include=['map_elites']),
      install_requires = ['numpy', 'scikit-learn',],
      )