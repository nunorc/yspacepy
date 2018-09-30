
from setuptools import setup, find_packages

setup(name='yspacepy',
      version='0.1',
      description='http://y-space.pw',
      url='https://github.com/y-space/yspacepy',
      author='Nuno Carvalho',
      author_email='narcarvalho@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['astropy'],
      zip_safe=False)

