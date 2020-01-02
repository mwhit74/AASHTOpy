from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='AASHTOpy',
      version='0.1',
      description='American Association of State Highway and Transportation Officials in Python',
      long_description=readme(),
      license='GPL 3.0',
      author='mlw',
      url='https://github.com/mwhit74/AASHTOpy',
      packages=[],
      install_requires=[])
