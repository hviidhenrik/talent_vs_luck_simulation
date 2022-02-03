from setuptools import find_packages, setup

setup(
    name="talent-vs-luck-sim",  # should not be the same name as the root folder
    version="0.2.0",
    description="Package with helper functions for PdM analysis",
    author="Henrik Hviid Hansen",
    author_email="hviidhenrik@outlook.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
)
