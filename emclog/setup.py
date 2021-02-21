import os
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="emclog",
    version="1.2.4",
    author="John Thornton",
    author_email="jt@gnipsel.com",
    description="Position Logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jethornton/7i96",
    download_url="https://github.com/jethornton/7i96/tarball/master",
    python_requires='>=2',
    platforms=['Posix'],
    packages=['emclog'],
    include_package_data=True,
    entry_points={
        'gui_scripts': ['emclog = emclog.emclog:main',],
    },
    data_files = [
        ('share/applications/', ['Position Logger.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: Qt",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
    ],
)
