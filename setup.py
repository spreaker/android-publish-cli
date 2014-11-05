
from __future__ import print_function
from setuptools import setup
import sys


if sys.version_info < (2, 6):
    print('google-api-python-client requires python version >= 2.6.', file = sys.stderr)
    sys.exit(1)

install_requires = ['google-api-python-client==1.3.1']

if sys.version_info < (2, 7):
    install_requires.append('argparse')

setup(
    name                = 'android-publish-cli',
    packages            = [],
    version             = '0.1.2',
    description         = 'A simple CLI for Google Play Publish API',
    author              = 'Spreaker',
    author_email        = 'dev@spreaker.com',
    url                 = 'https://github.com/spreaker/android-publish-cli',
    download_url        = 'https://github.com/spreaker/android-publish-cli/tarball/0.1.2',
    keywords            = ['android', 'automation', 'google'],
    classifiers         = [],
    install_requires    = install_requires,
    scripts             = ['bin/android-publish']
)