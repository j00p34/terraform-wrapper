import sys
from setuptools import setup

requires = ['botocore>=1.4.23',
            's3transfer>=0.0.1']

if sys.version_info[:2] == (2, 6):
    # Include argparse with python2.6
    requires.append('argparse>=1.1')

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tfwrapper',
    version='0.0.1a1',
    description='''
    Python wrapper for Terraform (https://www.terraform.io) that provides remote state management and basic locking
    ''',
    long_description=readme,
    author='David Harris',
    author_email='dharris@dharris.io',
    url='https://github.com/dharrisio/terraform-wrapper',
    scripts=['bin/terraform-wrapper'],
    install_requires=requires,
    extras_require={
        ':python_version=="2.6"': [
            'argparse>=1.1',
        ]
    },
    license=license,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ),
    packages=['terraform-wrapper']
)