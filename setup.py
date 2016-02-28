#!/usr/bin/env python

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='catchthecat',
    version='0.1',
    description='A cat on the loose in the house -- a simple text game.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
    ],
    url='http://pneumatic.readthedocs.org/',
    author='Anthony DeBarros',
    author_email='adebarros@gmail.com',
    license='MIT',
    packages=['catchthecat'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'catchthecat = catchthecat.catchthecat:start'
        ]
    }
)
