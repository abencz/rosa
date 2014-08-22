from setuptools import setup

def readme():
      with open('README.rst') as f:
            return f.read()

setup(name='rosa',
      version='0.1.3',
      description='Helper script for ROS',
      long_description=readme(),
      url='http://github.com/abencz/rosa',
      author='Alex Bencz',
      license='BSD',
      packages=['rosa'],
      scripts=['bin/rosa'],
      zip_safe=False)

