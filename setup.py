from setuptools import setup

setup(name='rosa',
      version='0.1.0',
      description='Helper script for ROS',
      url='http://github.com/abencz/rosa',
      author='Alex Bencz',
      license='BSD',
      packages=['rosa'],
      scripts=['bin/rosa'],
      zip_safe=False)

