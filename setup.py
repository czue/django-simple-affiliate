from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-simple-affiliate',
    version='0.1',
    description='Simple Affiliate System for Django',
    long_description=long_description,
    url='https://github.com/czue/django-simple-affiliate',
    author='Cory Zue',
    author_email='cory@coryzue.com',
    license='Apache Software License',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='affiliate marketing django middleware tracking',
    packages=find_packages(),
    install_requires=['django'],

    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
)
