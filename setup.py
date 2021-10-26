
# System imports
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='model_api',
      version='0.0.0.0',
      description='',
      long_description_content_type='text/markdown',
      packages=find_packages(),
      install_requires=requirements,
      include_package_data=True,
      zip_safe=False,
      requires=[])
