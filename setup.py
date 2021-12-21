from setuptools import setup, find_packages

setup(
    name='phd-package-name', # should not be the same name as the root folder
    version='0.1.0',
    description='Package with helper functions for PdM analysis',
    author='Henrik Hviid Hansen',
    author_email='hehha@orsted.dk',
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent", ],
    packages=find_packages(),
)



