# Copyright (C) 2018 HiPro IT Solutions Private Limited. All
# rights reserved.
#
# This program and the accompanying materials are made available under
# the terms described in the LICENSE file which accompanies this
# distribution. If the LICENSE file was not attached to this
# distribution or for further clarifications, please contact
# legal@hipro.co.in.

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'plaster_pastedeploy',
    'pyramid >= 1.9a',
    'pyramid_debugtoolbar',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.interface',
    'zope.sqlalchemy',
    'waitress',
    'cornice',
    'pyramid_jwt',
    'colander',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
    'requests',
]

setup(
    name='ttrack',
    version='2.0.dev0',
    description='TTrack',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='HiPro IT Solutions Private Limited',
    author_email='info@hipro.co.in',
    url='http://www.hipro.co.in',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = ttrack:main',
        ],
        'console_scripts': [
            'initialize_ttrack_db = ttrack.scripts.initializedb:main',
        ],
    },
)
